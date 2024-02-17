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
- **Requirements**: Login Required, Admin Required

### Upload Title Basics

- **Endpoint**: `/admin/upload/titlebasics`
- **Method**: POST
- **Description**: Uploads title basics data.
- **Requirements**: Login Required, Admin Required
- **Body**:
  - `tsv_data` (string, required): the tsv data you want to upload.

### Upload Title Akas

- **Endpoint**: `/admin/upload/titleakas`
- **Method**: POST
- **Description**: Uploads title akas data.
- **Requirements**: Login Required, Admin Required
- **Body**:
  - `tsv_data` (string, required): the tsv data you want to upload.

### Upload Name Basics

- **Endpoint**: `/admin/upload/namebasics`
- **Method**: POST
- **Description**: Uploads name basics data.
- **Requirements**: Login Required, Admin Required
- **Body**:
  - `tsv_data` (string, required): the tsv data you want to upload.

### Upload Title Crew

- **Endpoint**: `/admin/upload/titlecrew`
- **Method**: POST
- **Description**: Uploads title crew data.
- **Requirements**: Login Required, Admin Required
- **Body**:
  - `tsv_data` (string, required): the tsv data you want to upload.

### Upload Title Episode

- **Endpoint**: `/admin/upload/titleepisode`
- **Method**: POST
- **Description**: Uploads title episode data.
- **Requirements**: Login Required, Admin Required
- **Body**:
  - `tsv_data` (string, required): the tsv data you want to upload.

### Upload Title Principals

- **Endpoint**: `/admin/upload/titleprincipals`
- **Method**: POST
- **Description**: Uploads title principals data.
- **Requirements**: Login Required, Admin Required
- **Body**:
  - `tsv_data` (string, required): the tsv data you want to upload.

### Upload Title Ratings

- **Endpoint**: `/admin/upload/titleratings`
- **Method**: POST
- **Description**: Uploads title ratings data.
- **Requirements**: Login Required, Admin Required
- **Body**:
  - `tsv_data` (string, required): the tsv data you want to upload.

### Reset All

- **Endpoint**: `/admin/resetall`
- **Method**: POST
- **Description**: Resets all data.
- **Requirements**: Login Required, Admin Required

### User Modification

- **Endpoint**: `/admin/usermod/<string:username>/<string:password>`
- **Method**: POST
- **Description**: Modifies user information.
- **Requirements**: Login Required, Admin Required
- **Header**:
  - `username` (string, required): The username of the user.
  - `password` (string, required): The password of the user.

### User Info

- **Endpoint**: `/admin/users/<string:username>`
- **Method**: GET
- **Description**: Retrieves information about a specific user.
- **Requirements**: Login Required, Admin Required
- **Header**:
  - `username` (string, required): The username of the user.

## System Functionality Endpoints

### Get Title

- **Endpoint**: `/title/<string:titleID>`
- **Method**: GET
- **Description**: Retrieves information about a specific movie.
- **Requirements**: Login Required
- **Header**:
  - `titleID` (string, required): The titleID of the movie.


### Search Title

- **Endpoint**: `/searchtitle`
- **Method**: POST
- **Description**: Searches for movies based on a provided title part.
- **Requirements**: Login Required
- **Body**:
  - `titlePart` (string, required): The title part of the movie you are searching for.

### By Genre

- **Endpoint**: `/bygenre`
- **Method**: POST
- **Description**: Retrieves movies by genre and additional criteria.
- **Requirements**: Login Required
- **Body**:
  - `qgenre` (string, required): The genre of movie you are searching for.
  - `minrating` (float, required): The minimum rating for the movies.
  - `yrFrom` (int, required): Starting for year {yrFrom}.
  - `yrTo` (int, required): Ending up to year {yrTo}.


### Get Name

- **Endpoint**: `/name/<string:nameID>`
- **Method**: GET
- **Description**: Retrieves information about a specific person associated with movies.
- **Requirements**: Login Required
- **Body**:
  - `nameID` (string, required): The name of the person associated.

### Search Name

- **Endpoint**: `/searchname`
- **Method**: POST
- **Description**: Searches for names based on a provided name part.
- **Requirements**: Login Required
- **Body**:
  - `namePart` (string, required): The part of the name of the person associated you're searching for.

## Movie Rating Web App

### Rate Movie

- **Endpoint**: `/ratemovie`
- **Method**: POST
- **Description**: Allows users to rate movies.
- **Requirements**: Login Required
- **Body**:
  - `rating` (int, required): Like{1} or Dislike{-1} or (Unlike or Undislike){0}.
  - `title_id` (int, required): The title id of the title you're rating.

### Get Liked Movies

- **Endpoint**: `/getlikedmovies`
- **Method**: GET
- **Description**: Retrieves movies liked by the user.
- **Requirements**: Login Required

### Get Disliked Movies

- **Endpoint**: `/getdislikedmovies`
- **Method**: GET
- **Description**: Retrieves movies disliked by the user.
- **Requirements**: Login Required

### Get Top Rated Movies

- **Endpoint**: `/gettopratedmovies`
- **Method**: GET
- **Description**: Retrieves top-rated movies.
- **Requirements**: Login Required

## Extras

### Chat Bot

- **Endpoint**: `/chatbot`
- **Method**: POST
- **Description**: Interacts with a chatbot.
- **Requirements**: Login Required
- **Body**:
  -`Sentence` (string, required): The sentence the user used as input to the chatbot.

### User Role

- **Endpoint**: `/user_role`
- **Method**: GET
- **Description**: Retrieves the role of the current user.
- **Requirements**: Login Required

### Movie Recommender 1

- **Endpoint**: `/movierecommender_1/<string:title>`
- **Method**: GET
- **Description**: Recommends movies based on a provided title.
- **Requirements**: Login Required
- **Header**:
  -`title` (string, required): The title of the movie.

### Movie Recommender 2

- **Endpoint**: `/movierecommender_2/<string:genre>/<string:username>`
- **Method**: GET
- **Description**: Recommends movies based on a provided genre and username.
- **Requirements**: Login Required
- **Header**:
  -`genre` (string, required): The genre of the movie.
  -`username` (string, required): The username of the user.
  

