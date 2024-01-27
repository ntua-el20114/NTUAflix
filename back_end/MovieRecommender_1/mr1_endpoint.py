from flask import Flask, request, jsonify, make_response
from flask_restful import Resource
import pandas as pd
from io import StringIO
import secrets
from back_end import db
from ..auth import login_required, admin_required, getTitleObject
import json

from back_end.MovieRecommender_1.recommend import recommend

class Movie_Recommender_1(Resource):
    @login_required
    def get(self, user, title):
        return_list = recommend(title)
        final_list = []
        for title in return_list:
            try:
                cur = db.get_db().cursor()
                cur.execute("SELECT title_id from title where originalTitle=%s", [title])
                id = cur.fetchone()
                cur.close()
                print(id)
                result = getTitleObject(id["title_id"])
                final_list.append(result)
            except Exception as e:
                print(e)
                continue

        return_dict = {}
        return_dict["result"] = final_list

        json_result = json.dumps(return_dict, sort_keys=False)
        response = make_response(json_result, 200)
        return response
