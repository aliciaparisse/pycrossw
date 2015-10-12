#Main application : calls all the other files
import urllib2

def getMetWords(words):
    wordsGen = []
    query = "http://boundinanutshell.com/metaphor-magnet/q?kw=" + words + "&xml=true"
    data = urllib2.urlopen(query)
    content_text = data.read()
    return wordsGen;

def main():
    var = raw_input("Enter the two words from which you would like to generate >>")
    getMetWords(var)

    return;

if __name__ == "__main__":
    main()