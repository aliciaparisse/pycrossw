# File dedicated to create the crosswords from the words
from crossword_construction import main as mainC
from words_def import definitionRepresentation, getEmptyRepr
import math
from random import shuffle


def evaluateCrosswords(words, fitOption, nbIt, nbWords, length, height):
    bestFit = 0
    bestCw = []

    for i in xrange(nbIt):

        shuffle(words)

        #wordsAndDef = definitionRepresentation(words[:20],dictionnary)
        wordsAndDef = getEmptyRepr(words[:nbWords])

        crossword = mainC(wordsAndDef, length, height)
        a = fitness(crossword, fitOption)
        if a > bestFit:
            bestFit = a
            bestCw = crossword


    newWords = []
    for word in bestCw.current_word_list:
        newWords.append(str(word))

    return bestCw, newWords;

def fitness(crossword, option):
    #The crossword parameter represents the crossword
    #The option parameter represent the kind of fitness we want to apply

    if option == 0: #Option 0 is the number of words fitting in the crosswords
        return len(crossword.current_word_list);
    if option == 1: #Option 1 is the number of letters fitting in the crosswords
        fit =0
        for word in crossword.current_word_list:
            fit+= word.length
        return fit;
    if option == 2: #Option 2 is the function n^2 with n size of the word. The larger the word, the better
        fit = 0
        for word in crossword.current_word_list:
            fit+= math.pow(word.length,2)
        return fit;


