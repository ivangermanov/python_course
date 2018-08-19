import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    if word in data.keys():
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]

    while word not in data.keys():
        if word == "N":
            return "You have decided to stop using the translator."
        close_matches = get_close_matches(word, data.keys(), cutoff=0.8)
        if len(close_matches) > 1:
            return_cw = ""
            for cw in close_matches:
                if cw != close_matches[-1]:
                    if cw != close_matches[-2]:
                        return_cw += '"' + cw + '", '
                    else:
                        return_cw += '"' + cw + '" '
                else:
                    return_cw += 'or "' + cw + '"'

            word = input("Did you mean %s? Specify the word you wish to translate. If you want to quit, type \"N\"\n" % return_cw)

        elif len(close_matches) > 0:
            word = input("Did you mean \"%s\"? Specify the word you wish to translate. If you want to quit, type \"N\"\n" % close_matches[0])

        else:
            word = input("Word not found in the dictionary! Specify the word you wish to translate. If you want to quit, type \"N\"\n")
    
    return data[word]

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)