# Define column headers
column_headers_imdb_rating = ['title_id', 'averageRating', 'numVotes']

# Define data for imdb_rating table
data_1_imdb_rating = ('tt69', 5.3, 46)
data_2_imdb_rating = ('tt70', 5.2, 16)

# Create a list of tuples containing your data
all_data_imdb_rating = [data_1_imdb_rating, data_2_imdb_rating]

# Convert each tuple to a TSV string
tsv_data_list_imdb_rating = ['\t'.join([str(item) if item is not None else 'NULL' for item in data]) for data in all_data_imdb_rating]

# Join the column headers and the TSV data with newline characters
tsv_data_imdb_rating = '\t'.join(column_headers_imdb_rating) + '\n' + '\n'.join(tsv_data_list_imdb_rating)

# Write to the TSV file
with open('imdb_rating.tsv', 'w') as file:
    file.write(tsv_data_imdb_rating)
