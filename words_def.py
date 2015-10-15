#File dedicated to retrieving definition of words

import urllib
import json
from random import shuffle

api_key="0a191cb87c353380850028a93e705f18a8a1cebe13f4e8c15"
root_url="http://api.wordnik.com:80/v4"


def getDefinitions(word):

    query = root_url+"/word.json/" + word + "/definitions?"
    query  += "api_key=" + api_key
    print query
    data = urllib.urlopen(query)
    jsonDef = json.load(data)

    return jsonDef;

def getOneDefinition(word,dic):

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

    dic[word] = definition
    return definition;

def improve_definition(word):
    #Using the query /relatedWords, different types of related words are interesting
    #Synonymes, antonymes, hypernyms, hyponyms and same-context

    #We have two possible queries : either we choose to obtain the definition,
    #or we use some of the related words.

    #Dictionnary representing the different possibilities


    return 0;

def getEmptyRepr(words):
    repres = []
    for word in words:
        repres.append([word, " "])

    return repres;



def definitionRepresentation (words,dic):
    repres = []
    for word in words:
        if (word not in dic):
            defin = getOneDefinition(word,dic)
            if (defin != ""):
                repres.append([word,defin])
        else :
            repres.append([word,dic[word]])
    return repres;