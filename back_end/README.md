# API DOC

## Base URL
https::/localhost:PORT/ntuaflix\_api/


## User Access Endpoints

### Login

- **Endpoint**: `/login`
- **Method**: POST
- **Description**: Allows users to log in.
- **Parameters**:
  - `username` (string, required): The username of the user.
  - `password` (string, required): The password of the user.

### Logout

- **Endpoint**: `/logout`
- **Method**: POST
- **Description**: Logs out the current user.

### Get App User Data

- **Endpoint**: `/getappuserdata`
- **Method**: GET
- **Description**: Retrieves data related to the current user.

## Admin Endpoints

### Health Check

- **Endpoint**: `/admin/healthcheck`
- **Method**: GET
- **Description**: Performs a health check on the API.

### Upload Title Basics

- **Endpoint**: `/admin/upload/titlebasics`
- **Method**: POST
- **Description**: Uploads title basics data.

### Upload Title Akas

- **Endpoint**: `/admin/upload/titleakas`
- **Method**: POST
- **Description**: Uploads title akas data.

### Upload Name Basics

- **Endpoint**: `/admin/upload/namebasics`
- **Method**: POST
- **Description**: Uploads name basics data.

### Upload Title Crew

- **Endpoint**: `/admin/upload/titlecrew`
- **Method**: POST
- **Description**: Uploads title crew data.

### Upload Title Episode

- **Endpoint**: `/admin/upload/titleepisode`
- **Method**: POST
- **Description**: Uploads title episode data.

### Upload Title Principals

- **Endpoint**: `/admin/upload/titleprincipals`
- **Method**: POST
- **Description**: Uploads title principals data.

### Upload Title Ratings

- **Endpoint**: `/admin/upload/titleratings`
- **Method**: POST
- **Description**: Uploads title ratings data.

### Reset All

- **Endpoint**: `/admin/resetall`
- **Method**: POST
- **Description**: Resets all data (unfinished).

### User Modification

- **Endpoint**: `/admin/usermod/<string:username>/<string:password>`
- **Method**: POST
- **Description**: Modifies user information.

### User Info

- **Endpoint**: `/admin/users/<string:username>`
- **Method**: GET
- **Description**: Retrieves information about a specific user.

## System Functionality Endpoints

### Get Title

- **Endpoint**: `/title/<string:titleID>`
- **Method**: GET
- **Description**: Retrieves information about a specific movie.

### Search Title

- **Endpoint**: `/searchtitle`
- **Method**: POST
- **Description**: Searches for movies based on a provided title part.

### By Genre

- **Endpoint**: `/bygenre`
- **Method**: POST
- **Description**: Retrieves movies by genre and additional criteria.

### Get Name

- **Endpoint**: `/name/<string:nameID>`
- **Method**: GET
- **Description**: Retrieves information about a specific person associated with movies.

### Search Name

- **Endpoint**: `/searchname`
- **Method**: POST
- **Description**: Searches for names based on a provided name part.

## Movie Rating Web App

### Rate Movie

- **Endpoint**: `/ratemovie`
- **Method**: POST
- **Description**: Allows users to rate movies.

### Get Liked Movies

- **Endpoint**: `/getlikedmovies`
- **Method**: GET
- **Description**: Retrieves movies liked by the user.

### Get Disliked Movies

- **Endpoint**: `/getdislikedmovies`
- **Method**: GET
- **Description**: Retrieves movies disliked by the user.

### Get Top Rated Movies

- **Endpoint**: `/gettopratedmovies`
- **Method**: GET
- **Description**: Retrieves top-rated movies.

## Extras

### Chat Bot

- **Endpoint**: `/chatbot`
- **Method**: POST
- **Description**: Interacts with a chatbot.

### User Role

- **Endpoint**: `/user_role`
- **Method**: GET
- **Description**: Retrieves the role of the current user.

### Movie Recommender 1

- **Endpoint**: `/movierecommender_1/<string:title>`
- **Method**: GET
- **Description**: Recommends movies based on a provided title.

### Movie Recommender 2

- **Endpoint**: `/movierecommender_2/<string:genre>/<string:username>`
- **Method**: GET
- **Description**: Recommends movies based on a provided genre and username.

