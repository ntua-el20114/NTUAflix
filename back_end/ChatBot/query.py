import mysql.connector



def print_movie(actor):
    string = ""
    for item in actor:
        string += item + " "
    string = string.rstrip()
    print(string)

# Define the SQL query
# Establish a connection to your MySQL database
    cnx = mysql.connector.connect(
        host='localhost',
        # user='peteraugerinos',
        user='root',
        database='ntuaflix'
    )

# Create a cursor object to execute queries
    cursor = cnx.cursor()
    query = f"""
        SELECT title.*
        FROM title
        JOIN name_title ON title.title_id = name_title.title_id
        JOIN name ON name.name_id = name_title.name_id
        WHERE name.primaryName = '{string}';
    """
    try:
        # Execute the query
        cursor.execute(query)

        # Fetch all the rows
        movies = cursor.fetchall()

        if movies:
            # Displaying movie information
            for movie in movies:
                print(movie)  # Adjust how you want to display the movie details

        else:
            print(f"No movies found for {string}.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Close the cursor and connection
    cursor.close()
    cnx.close()
