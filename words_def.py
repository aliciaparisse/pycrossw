# File dedicated to retrieving definition of words

import urllib
import json
from random import shuffle

api_key = "0a191cb87c353380850028a93e705f18a8a1cebe13f4e8c15"
root_url = "http://api.wordnik.com:80/v4"

# Dictionnary representing the different possibilities(used for function improved_definition)
options = {0: "def", 1: "synonym", 2: "antonym", 3: "hypernym", 4: "hoponym", 5: "same-context", 6: "equivalent"}


def getOneDefinition(word, dic, json):
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


# Function needed to construct the dictionnary
def improved_definition(word, dic):
    # Using the query /relatedWords, different types of related words are interesting
    # Synonymes, antonymes, hypernyms, hyponyms and same-context

    # We have two possible queries : either we choose to obtain the definition,
    # or we use some of the related words.

    # Initialization of variables
    definition = ""
    nbNone = 0

    # Randomly choosing the option
    indexes = list(xrange(7))

    while indexes:
        shuffle(indexes)
        option = indexes[0]

        if option == 0:  # Plain definition

            # Query to the API ------------------------------------
            query = root_url + "/word.json/" + word + "/definitions?"
            query += "api_key=" + api_key
            data = urllib.urlopen(query)
            jsonDef = json.load(data)

            # Getting just one definition
            definition = getOneDefinition(word, dic, jsonDef)

        else:  # Synonym, antonym, hepernym, hoponym or same-context words
            # Query to the API ------------------------------------
            query = root_url + "/word.json/" + word + "/relatedWords?"
            query += "api_key=" + api_key
            query += "&limitPerRelationshipType=10"
            data = urllib.urlopen(query)
            jsonObj = json.load(data)

            # Getting the list of words from the option we choose
            for relation in jsonObj:
                if relation["relationshipType"] == options[option]:
                    definition = relation["words"]
                    break

        if definition != "":
            break
        else:
            indexes.remove(option)

    if definition == "":
        definition = "None"
        nbNone += 1

    return definition, option;


# Function needed to launch the crosswords
def getEmptyRepr(words):
    repres = []
    for word in words:
        repres.append([word, " "])

    return repres;


def representationFitness(triedOptions):
    r = 1.0 / 7.0
    target = [r, r, r, r, r, r, r]

    # Getting the  result in  the same  form as the target
    result = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    for i in xrange(len(triedOptions)):
        result[triedOptions[i]] += 1.0
    result = [x / float(len(triedOptions)) for x in result]

    # Calculating the fitness
    fit = 0
    for i in xrange(len(target)):
        fit += abs(target[i] - result[i])

    return fit;

def getBestDefs (words,dic, nbIt):
    bestFit = len (words)

    for i in xrange(nbIt):
        [repres, triedOptions] = definitionRepresentation(words, dic)

        fitness = representationFitness(triedOptions)
        print fitness
        if fitness < bestFit:
            bestRep = repres
            bestFit = fitness

    return bestRep;

def definitionRepresentation(words, dic):
    dic = {}
    triedOptions = []

    repres = []
    for word in words:
        if (word not in dic):
            [defin, opt] = improved_definition(word, dic)
            triedOptions.append(opt)
            if (defin != ""):
                repres.append([word, defin])
        else:
            repres.append([word, dic[word]])


    return repres, triedOptions;
