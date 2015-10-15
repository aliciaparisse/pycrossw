#File dedicated to retrieving definition of words

import urllib
import json
from random import shuffle

api_key="0a191cb87c353380850028a93e705f18a8a1cebe13f4e8c15"
root_url="http://api.wordnik.com:80/v4"

#Dictionnary representing the different possibilities(used for function improved_definition)
options = { 0 : "def", 1 : "synonym", 2 : "antonym", 3 : "hypernym", 4 : "hoponym", 5 : "same-context", 6: "equivalent"}



def getDefinitions(word):

    query = root_url+"/word.json/" + word + "/definitions?"
    query  += "api_key=" + api_key
    print query
    data = urllib.urlopen(query)
    jsonDef = json.load(data)

    return jsonDef;

def getOneDefinition(word,dic,json):

    definition = ""

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

def improved_definition(word,dic):
    #Using the query /relatedWords, different types of related words are interesting
    #Synonymes, antonymes, hypernyms, hyponyms and same-context

    #We have two possible queries : either we choose to obtain the definition,
    #or we use some of the related words.

    #Initialization of variables
    definition = ""
    nbNone=0

    #Randomly choosing the option
    indexes = list(xrange(7))
    shuffle(indexes)
    option = indexes[0]

    if option == 0: #Plain definition

        #Query to the API ------------------------------------
        query = root_url+"/word.json/" + word + "/definitions?"
        query  += "api_key=" + api_key
        data = urllib.urlopen(query)
        jsonDef = json.load(data)

        #Getting just one definition
        definition = getOneDefinition(word,dic,jsonDef)

    else : #Synonym, antonym, hepernym, hoponym or same-context words
        res = []
        #Query to the API ------------------------------------
        query = root_url+"/word.json/" + word + "/relatedWords?"
        query  += "api_key=" + api_key
        query  += "&limitPerRelationshipType=10"
        data = urllib.urlopen(query)
        jsonObj = json.load(data)

        #Getting the list of words from the option we choose
        for relation  in jsonObj:
            if relation["relationshipType"] == options[option]:
                res = relation["words"]
                break

        if  res == []:
            definition = "None"
            nbNone +=1

    return definition;

#Function needed to launch the crosswords
def getEmptyRepr(words):
    repres = []
    for word in words:
        repres.append([word, " "])

    return repres;



def definitionRepresentation (words,dic):
    dic =  {}

    repres = []
    for word in words:
        if (word not in dic):
            defin = improved_definition(word,dic)
            if (defin != ""):
                repres.append([word,defin])
        else :
            repres.append([word,dic[word]])
    return repres;