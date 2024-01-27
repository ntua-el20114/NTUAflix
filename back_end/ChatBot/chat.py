import random
import json
import torch
from model import NeuralNet
from nltk_utils import tokenize,bag_of_words
from extractor import extract_actors, extract_genres
from query import print_movie



FILE = "./data.pth"


with open('intents.json','r') as f:
  intents = json.load(f)

data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

bot_name = "Tao"
print("Let's chat! To stop type 'quit'!")
while(True):
    sentence = input('You: ')
    actors = extract_actors(sentence)
    if sentence == "quit":
      break
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if actors:
        print_movie(actors)
    else:
        if prob.item() > 0.75:
            for intent in intents["intents"]:
                if tag == intent['tag']:
                    print(f'{bot_name}: {random.choice(intent["responses"])}')
        else:
            print(f'{bot_name}: {random.choice(intents["intents"][-1]["responses"])}')

