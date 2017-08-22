import json
from difflib import get_close_matches

# Load the data file
data = json.load(open("data.json"))

# Lookup input(str) in data file and return either a definition or an error
def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean \"%s\" instead? Enter 'Y' if yes, or 'N' if no: " % get_close_matches(word, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == "n":
            return "Sorry, \"" + word + "\"" + " does not exist in the dictionary."
        else:
            return "We didn't understand your entry."
    else:
        return "Sorry, \"" + word + "\"" + " does not exist in the dictionary."

# Request for user input
word = input("Enter word: ")

# Print the definition or error message to the CLI
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)