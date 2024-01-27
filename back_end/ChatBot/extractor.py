import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

genre_keywords = ['Action','Adult','Adventure','Animation','Biography','Comedy','Crime','Documentary',
                 'Drama','Family','Fantasy','History','Horror','Music','Musical','Mystery','News',
                 'Romance','Sci-Fi','Short','Sport','Thriller','War','Western', 'action','adult',
                  'adventure','animation','biography','comedy','crime','documentary',
                 'drama','family','fantasy','history','horror','music','musical','mystery','news',
                 'romance','sci-fi','short','sport','thriller','war','western']

def extract_actors(text):
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    actors = [word for word, tag in tagged_tokens if tag == 'NNP']  # Extract proper nouns (NNP)
    return actors

def extract_genres(text):
    tokens = word_tokenize(text.lower())
    genres = [token for token in tokens if token in genre_keywords]
    return genres

user_input = "Can you tell me about action movies ?"
actors = extract_genres(user_input)

print(actors)
