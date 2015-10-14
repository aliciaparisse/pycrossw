# File dedicated to create the crosswords from the words

def commonLetters(s1, s2):
    l1=list(''.join(s1.split()))
    l2=list(''.join(s2.split()))
    return [x for x in l1 if x in l2]

def evaluateCrosswords(words):
    return 0;