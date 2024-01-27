from back_end import db

# username will be specified according to the user
# Here, we assume the following username
# We find the user_id with the query a few lines below

# Suppose that we have username
# Get the corresponding id


##
# A function that gets a specific genre and returns some recommendations
# The functions assumes that the user id is specified before the function usage
#
# It takes two parameters:
#   genre (str) -> genre the user chooses to see
#   no_recommendations (int) -> number of recommendations the user wants to appear
#
# The function:
#   prints the the top recommendation movies
#   returns the id's for top recommendation movies
# 
# return type -> list of str's
##
def recommend_by_genre(genre, username ,no_recommendations=3):

    if genre == None:
        print("Please specify your wanted genre\n")

    c = db.get_db().cursor()
    c.execute(f"SELECT id FROM app_user WHERE username = '{username}'")
    result = c.fetchall()
    user_id = result[0]['id']
    
    # Select all movies with the wanted genre that the user has not pressed the like button yet
    c.execute(f"SELECT title_id, originalTitle FROM title "
              f"WHERE title.title_id NOT IN "
              f"(SELECT user_preferences.title_id FROM user_preferences WHERE user_preferences.user_id = '{user_id}') "
              f"AND title.genres LIKE '%{genre}%'")
    
    # Fetch all the rows
    title_id_genre = c.fetchall()
    #print(title_id_genre)
    ratings = {}
    titles = {}
    for row in title_id_genre:

        # Check NULL values
        if row['title_id'] is None or row['originalTitle'] is None:
            continue

        temp_title_id = row['title_id']
        temp_title = row['originalTitle']
        titles[temp_title_id] = temp_title

        # Get the average rating for current movie
        c.execute(f"SELECT averageRating FROM imdb_rating WHERE title_id = '{temp_title_id}'")
        temp_rating = c.fetchall()

        # Check NULL ratings
        if len(temp_rating) == 0:
            continue

        temp_rating = temp_rating[0]['averageRating']
        ratings[temp_title_id] = temp_rating

    c.close()
    

    # Sort in descending order and keep the top rated movies in that gerne
    ratings = dict(sorted(ratings.items(), key=lambda item: item[1], reverse=True))
    top_ratings = dict(list(ratings.items())[:no_recommendations])
    #top_ids = [] # will have the id's for the top rated movies

    #print("\nHere are the best recommendations for you")
    #print("-------------------------------------------")
    # Initialize an empty list to store dictionaries
    recommendations_list = []
    for temp_title_id in top_ratings:
        #top_ids.append(temp_title_id)
        temp_title = titles[temp_title_id]
        temp_rating = ratings[temp_title_id]        
        # Create a dictionary for each movie
        movie_dict = {
            'id': temp_title_id,
            'title': temp_title,
            'rating': temp_rating
        }
        #print(f"'{temp_title_id}' '{temp_title}' '{temp_rating}'\n")
        # Append the dictionary to the list
        recommendations_list.append(movie_dict)
    
    return recommendations_list

# Example usage:
# username = 'ColemanAlisa32'
# recommendations = recommend_by_genre("Documentary", username)
# print(recommendations)
