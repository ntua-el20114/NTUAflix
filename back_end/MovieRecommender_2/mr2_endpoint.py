from flask import Flask, request, jsonify, make_response
from flask_restful import Resource
import pandas as pd
from io import StringIO
import secrets
from back_end import db
from ..auth import login_required, admin_required, getTitleObject
import json
from flask_cors import cross_origin

from back_end.MovieRecommender_2.recommend_by_genre import recommend_by_genre

class Movie_Recommender_2(Resource):
    @cross_origin()
    @login_required
    def get(self, user, genre, username):
        return_list = recommend_by_genre(genre, username)
        final_list = []
        for item in return_list:
            id = item["id"]
            result = getTitleObject(id)
            final_list.append(result)

        return_dict = {}
        return_dict["result"] = final_list
        json_result = json.dumps(return_dict, sort_keys=False)
        response = make_response(json_result, 200)
        return response
