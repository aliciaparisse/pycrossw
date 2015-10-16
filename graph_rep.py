#File dedicated to the graphical representation

def defRepresentation(repres):
    stream = "\n"
    for i in xrange(len(repres)):
        stream += str(i+1) + ". " + repres[i][1] + "\n"

    return stream;
