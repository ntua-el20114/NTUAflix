from flask import Flask, request, jsonify, make_response
from flask_restful import Resource
import pandas as pd
from io import StringIO
import secrets
from back_end import db
from ..auth import login_required, admin_required
import random
import json
import torch
import os
from .model import NeuralNet
from .nltk_utils import tokenize,bag_of_words
from .extractor import extract_actors, extract_genres
from .query import print_movie

class ChatBot(Resource):
    @login_required
    def get(self, user):
        script_dir = os.path.dirname(__file__)
        intents_path = os.path.join(script_dir, 'intents.json')
        data_path = os.path.join(script_dir, 'data.pth')
        sentence = request.form.get('Sentence')
        actors = extract_actors(sentence)
        genres = extract_genres(sentence)
        FILE = data_path

        with open(intents_path,'r') as f:
          intents = json.load(f)

        data = torch.load(FILE)

        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]
        all_words = data["all_words"]
        tags = data["tags"]
        model_state = data["model_state"]

        model = NeuralNet(input_size, hidden_size, output_size)
        model.load_state_dict(model_state)
        model.eval()
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if genres:
            response = "Maybe you'll enjoy these movies: "
            string = ""
            for item in genres:
                string += item + " "
            string = string.rstrip()
            query = f"""
                    SELECT title.*
                    FROM title
                    WHERE genres = '{string}';
                    """
            cur = db.get_db().cursor()
            cur.execute(query)
            results = cur.fetchall()
            if results:
                for result in results:
                    if result["originalTitle"] != None:
                        response += "{"
                        response += result["originalTitle"]
                        response += "}"
                    else:
                        continue
                cur.close()
            else:
                cur.close()
                return {"Response": "No movies with such genre found"},200

            return {"Response": response},200

        if actors:
            response = "Maybe you'll enjoy these movies: "
            string = ""
            for item in actors:
                string += item + " "
            string = string.rstrip()
            query = f"""
                    SELECT title.*
                    FROM title
                    JOIN principals ON title.title_id = principals.title_id
                    JOIN name ON name.name_id = principals.name_id
                    WHERE name.primaryName = '{string}';
                    """
            cur = db.get_db().cursor()
            cur.execute(query)
            results = cur.fetchall()
            if results:
                for result in results:
                    if result["originalTitle"] != None:
                        response += "{"
                        response += result["originalTitle"]
                        response += "}"
                    else:
                        continue
                cur.close()
            else:
                cur.close()
                return {"Response":"No movies with such actor found."},200

            return {"Response": response},200

        if prob.item() > 0.75:
            for intent in intents["intents"]:
                if tag == intent['tag']:
                    return {'Response':f'{random.choice(intent["responses"])}'},200
        else:
            return {'Response':f'{random.choice(intents["intents"][-1]["responses"])}'},200
