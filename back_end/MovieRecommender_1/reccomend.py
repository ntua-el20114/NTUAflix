import pickle



def recommend(movie):
     new_title = pickle.load(open(r"C:\Users\Gregory Delatolas\Documents\GitHub\softeng23-44\back-end\MovieRecommender_1\movies_list.pkl", 'rb'))
     ratings = pickle.load(open(r"C:\Users\Gregory Delatolas\Documents\GitHub\softeng23-44\back-end\MovieRecommender_1\ratings.pkl", 'rb'))
     similarity = pickle.load(open(r"C:\Users\Gregory Delatolas\Documents\GitHub\softeng23-44\back-end\MovieRecommender_1\similarity.pkl", 'rb'))
     #movies_list = new_title['title'].values
     index = int(new_title[new_title['title'] == movie].index[0])
     distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
     j = 0
     counter = 0
     recommend_movies = []  
     while counter <= 10 and j <= 500:
          i = distance[j]
          j = j+1
          title_id = new_title.iloc[i[0]].title_id
          avg_rating_series = ratings[ratings['title_id'] == title_id]['averageRating']
          
          if avg_rating_series.empty or new_title.loc[i[0]]['title'] == movie:
               continue
          counter += 1
          
          avg_rating = avg_rating_series.iloc[0] 

          recommend_movies.append({
               'title': new_title.iloc[i[0]].title,
               'avg_rating': avg_rating
          })

     # Sort recommend_movies based on avg_rating
     sorted_movies = sorted(recommend_movies, key=lambda x: x['avg_rating'], reverse=True)
     # Extract only 'title' information
     recommend_titles = [temp['title'] for temp in sorted_movies]
     recommend__titles = recommend_titles[0:5]
     return recommend__titles



if __name__ == "__main__":
    pass
    #main()



"""def main():
     

     movie_title = input('Input a movie title: ')
     test_list = []
     test_list = recommend(movie_title)
     print(test_list)
"""