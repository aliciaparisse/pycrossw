#File dedicated to retrieving definition of words

import urllib
import json
from random import shuffle

api_key="0a191cb87c353380850028a93e705f18a8a1cebe13f4e8c15"
root_url="http://api.wordnik.com:80/v4"


def getDefinitions(word):

    query = root_url+"/word.json/" + word + "/definitions?"
    query  += "api_key=" + api_key
    data = urllib.urlopen(query)
    jsonDef = json.load(data)

    return jsonDef;

def getOneDefinition(word):

    definition = ""

    json = getDefinitions(word)
    l = len(json)
    indexes = list(xrange(l))
    shuffle(indexes)

    for i in xrange(l):
        definition = json[indexes[0]]["text"]
        if word in definition:
            indexes.remove(indexes[0])
            shuffle(indexes)
        else:
            break

    return definition;

def definitionRepresentation (words):
    repres = []
    for word in words:
        if (getOneDefinition(word) != ""):
            repres.append([word,getOneDefinition(word)])

    return repres;