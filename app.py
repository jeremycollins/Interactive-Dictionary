import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "\"" + word + "\"" + " does not exist in the dictionary."

word = input("Enter word: ")

print(translate(word))
