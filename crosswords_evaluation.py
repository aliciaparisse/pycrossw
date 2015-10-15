# File dedicated to create the crosswords from the words
from crossword_construction import main as mainC
from words_def import definitionRepresentation, getEmptyRepr
import math
from random import shuffle

from deap import algorithms
from deap import base
from deap import creator
from deap import tools


def evaluateCrosswords(words, fitOption):
    bestFit = 0
    bestCw = []

    for i in xrange(5):

        shuffle(words)

        #wordsAndDef = definitionRepresentation(words[:20],dictionnary)
        wordsAndDef = getEmptyRepr(words[:20])

        crossword = mainC(wordsAndDef)
        a = fitness(crossword, fitOption)
        if a > bestFit:
            bestFit = a
            bestCw = crossword

    print bestFit
    return bestCw;

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



# def createIndividual(words,dic):
#     shuffle(words)
#
#     wordsAndDef = definitionRepresentation(words[:20], dic)
#     crossword = mainC(wordsAndDef)
#
#     return crossword;
#
# def getGeneticBestCrosswords(words):
#
#     word_dic ={}
#
#     def eval(individual):
#         #Evaluate individual
#         fit = individual.current_word_list
#         return fit,
#
#     creator.create("FitnessMin", base.Fitness, weights=(1.0,))
#     creator.create("Individual", list, fitness=creator.FitnessMin)
#
#     toolbox = base.Toolbox()
#
#     nb = random.randint(50,75)
#     toolbox.register('random_digit', random.randint,50,75)
#     toolbox.register('create_individual', createIndividual,words, word_dic)
#     toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.create_individual, n =nb)
#     toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#
#     toolbox.register("evaluate", eval)
#
#     toolbox.register("select", tools.selBest)
#
#     toolbox.register("mate", tools.cxOnePoint)
#
#     def mutate(individual):
#     #     #Mutated individual
#     #     new = createIndividual(p,d,o)
#     #     #Randomly change a note in the individual
#     #     individual[(random.randint(0,len(individual)-1))] =  new
#     #
#     #     return individual,
#
#         return individual,
#
#     toolbox.register("mutate", mutate)
#
#     generations = 1
#     pop = toolbox.population(n=2)
#     hof = tools.HallOfFame(1)
#
#     #Normal  0.6260 - 0.6360
#     #1000 pop 0.6322 - 0.640
#     #1000 gen 0.638 - 0.6440
#     import numpy as np
#     stats = tools.Statistics(lambda ind: ind.fitness.values)
#     stats.register("avg", np.mean)
#     stats.register("std", np.std)
#     stats.register("min", np.min)
#     stats.register("max", np.max)
#
#     crossover_prob = 0.8
#     mutation_prob = 0.0
#
#     algorithms.eaSimple(pop, toolbox, crossover_prob, mutation_prob, generations, stats, halloffame=hof)
#     a = hof[0]
#     return eval(hof[0]);
