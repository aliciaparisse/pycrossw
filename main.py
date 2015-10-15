# Main application : calls all the other files
import urllib
from lxml import etree
from crosswords_evaluation import evaluateCrosswords


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
            wordsGen.append(str[i + 1:])
            wordsGen.append(str[:i])
    return wordsGen;


def main():
    # var = raw_input("Enter the two words from which you would like to generate >>")
    var = "love"
    words = getMetWords(var)

    evaluateCrosswords(words,1)
    return;


if __name__ == "__main__":
    main()
