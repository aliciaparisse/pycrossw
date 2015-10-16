# Main application : calls all the other files
import urllib
from lxml import etree
from crosswords_evaluation import evaluateCrosswords
from words_def import getBestDefs
from graph_rep import defRepresentation


def getMetWords(words):
    wordsGen = []
    query = "http://ngrams.ucd.ie/metaphor-magnet-acl/q?kw=" + '+'.join(words.split(' ')) + "&xml=true"
    data = urllib.urlopen(query)
    content_text = data.read()

    root = etree.fromstring(content_text)
    for child in root:
        for elem in child.findall("Text"):
            str = elem.text.strip()
            i = str.find(":")
            if (str[i + 1 :] not in wordsGen) and ("_" not in str[i + 1 :]):
                wordsGen.append(str[i + 1:])
            if (str[:i] not in wordsGen) and ("_" not in str[:i]):
                wordsGen.append(str[:i])
    return wordsGen;


def main():
    dictionnary = {}
    # var = raw_input("Enter the two words from which you would like to generate >>")
    var = "love"
    words = getMetWords(var)

    #You can change the parameters of this function -----------------
    #First parameter you can't change, because it's generated from the choose word
    #Second parameter is the kind of evaluation you want to choose
    # for the improvement of your crossword:
    #       --> 0 : fitness based on the number of words inside the crosswords
    #       --> 1 : fitness based on the number of letters inside the crosswords
    #       --> 2 : fitness based on the square of nb of letters per word
    #Third parameter is the number of times you want to create crosswords
    # (always trying to find a better crossword)
    #Fourth parameter is the number of words that you can choose from the list of words
    # if the number of words is high, it will take a longer time, but the results will be better
    #Fifth and sixth parameters are (in this order) the length and the height of the crossword.

    [bestCw, selectedWords] = evaluateCrosswords(words, 2, 5, 40, 13,13)

    #You can change the parameters of this function -----------------
    #First and second parameters you can't change
    #Third parameter represents the number of iterations you want to do
    # In each iteration, all the definitions are created anew.
    #Fourth parameter is called help. If this parameter is set to True
    # then the clues are more precise. For exemple, we tell
    repres = getBestDefs(selectedWords, 20, True)

    print bestCw.current_word_list
    print bestCw.solution()
    print defRepresentation(repres)

    return;


if __name__ == "__main__":
    main()
