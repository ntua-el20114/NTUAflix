from flask_restful import Api

from back_end import app
from .auth import *
from .admin import *
from .ChatBot.chatbot_endpoint import *
from .MovieRecommender_1.mr1_endpoint import *
from .MovieRecommender_2.mr2_endpoint import *
from flask_cors import CORS

api = Api(app, prefix='/ntuaflix_api')
CORS(app, resources={r"/ntuaflix_api/*": {"origins": "http://127.0.0.1:9876"}})

#User Access Endpoints
api.add_resource(UserLogin, '/login') #takes body/form parameters username,password
api.add_resource(UserLogout, '/logout')
api.add_resource(GetAppUserData, '/getappuserdata')

# Admin Endpoints
api.add_resource(HealthCheck, '/admin/healthcheck') #1
api.add_resource(TitleBasics, '/admin/upload/titlebasics') #2
api.add_resource(TitleAkas, '/admin/upload/titleakas') #3
api.add_resource(NameBasics, '/admin/upload/namebasics') #4
api.add_resource(TitleCrew, '/admin/upload/titlecrew') #5
api.add_resource(TitleEpisode, '/admin/upload/titleepisode') #6
api.add_resource(TitlePrincipal, '/admin/upload/titleprincipals') #7
api.add_resource(TitleRatings, '/admin/upload/titleratings') #8
api.add_resource(ResetAll, '/admin/resetall') #9 (unfinished)
api.add_resource(UserMod, '/admin/usermod/<string:username>/<string:password>') #10
api.add_resource(UserInfo, '/admin/users/<string:username>') #11

#System's Functionality Endpoints
api.add_resource(GetTitle, '/title/<string:titleID>') #A takes url parameter titleID
api.add_resource(SearchTitle, '/searchtitle') #B , takes body/form parameter titlePart
api.add_resource(ByGenre, '/bygenre') #C takes body/form parameter gqueryObject(qgenre,minrating,yrFrom(opt),yrTo(opt))
api.add_resource(GetName, '/name/<string:nameID>') #D takes url parameter nameID
api.add_resource(SearchName, '/searchname') #E takes body/form parameter namePart

#Movie Rating Web App
api.add_resource(RateMovie, '/ratemovie')
api.add_resource(GetLikedMovies, '/getlikedmovies')
api.add_resource(GetDislikedMovies, '/getdislikedmovies')
api.add_resource(GetTopRatedMovies, '/gettopratedmovies')

#Extras
api.add_resource(ChatBot, '/chatbot')
api.add_resource(UserRole, '/user_role')
api.add_resource(Movie_Recommender_1, '/movierecommender_1/<string:title>')
api.add_resource(Movie_Recommender_2, '/movierecommender_2/<string:genre>/<string:username>')

if __name__ == "__main__":  
    # debug mode: every time we change it restarts the server
    app.run(debug=True, port=9876)
