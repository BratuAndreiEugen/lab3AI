import copy

import networkx as nx

from geneticAlgorithm.chromosome import Chromosome
from geneticAlgorithm.ga import GA
from geneticAlgorithm.ga_no_heap import GASimple
from geneticAlgorithm.modularity import modularity, modularity1, modularity2
from graphics.graphs import plotNetwork
from utils.gmlReader import reader


def community_genetic_algorithm(network, generations, popSize):
    noNodes = len(nx.nodes(network))
    noEdges = len(nx.edges(network))
    m = nx.adjacency_matrix(network)
    matrix = m.todense() # matricea de adiacenta
    usableNetwork = {}
    usableNetwork['noNodes'] = noNodes
    usableNetwork['noEdges'] = noEdges
    usableNetwork['matrix'] = matrix
    deg = (noNodes) * [0]  # initializare vector
    i = 0
    for x in nx.degree(network):
        deg[i] = x[1]
        i = i + 1

    usableNetwork['degrees'] = deg

    usableNetwork['function'] = modularity
    populationParams = {}
    populationParams['popSize'] = popSize
    ga = GA(populationParams, usableNetwork)
    ga.initialisation()
    ga.evaluation()
    numberOfGenerations = generations
    bestOverAll = Chromosome(usableNetwork)
    bestOverAll.fitness = -2
    while numberOfGenerations > 0:
        numberOfGenerations -= 1
        ga.oneGenerationElitism2()
        best = ga.bestChromosome()
        print(best)
        if best.fitness > bestOverAll.fitness:
            bestOverAll.repres = copy.deepcopy(best.repres)
            bestOverAll.fitness = best.fitness

    print(bestOverAll)
    print(len(set(bestOverAll.repres)))
    return bestOverAll

def solver(path, name, gen, pop):
    net = reader(path)
    r = community_genetic_algorithm(net, gen, pop)
    plotNetwork(net, r.repres, name + " " + str(len(set(r.repres))) + " Generatii " + str(gen) + " PopSize " + str(pop))

# with modularity()
# GIVEN TESTS
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\karate\\karate.gml", "KARATE", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\dolphins\\dolphins.gml", "DOLPHINS", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\krebs\\krebs.gml", "KREBS", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\football\\football.gml", "FOOTBALL", 300, 300)
#
# # MY TESTS
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test1.gml", "CHATGPT", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test2.gml", "LES MISERABLES", 300, 300)
solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test3.gml", "CO-AUTHORSHIPS", 500, 100)
#solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test4.gml", "NEURAL NETWORK", 500, 100)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test5.gml", "POLITICAL BLOGS", 300, 300)
#solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\polbooks.gml", "POLITICAL BOOKS", 300, 300)

#with modularity1()
# #GIVEN TESTS
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\karate\\karate.gml", "KARATE", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\dolphins\\dolphins.gml", "DOLPHINS", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\krebs\\krebs.gml", "KREBS", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\football\\football.gml", "FOOTBALL", 300, 300)
#
# # MY TESTS
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test1.gml", "CHATGPT", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test2.gml", "LES MISERABLES", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test4.gml", "NEURAL NETWORK", 500, 100)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\polbooks.gml", "POLITICAL BOOKS", 300, 300)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test6.gml", "WORLD ADJACENCIES", 300, 300)


#with modularity2()
#GIVEN TESTS
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\karate\\karate.gml", "KARATE", 1000, 50)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\dolphins\\dolphins.gml", "DOLPHINS", 300, 50)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\krebs\\krebs.gml", "KREBS", 300, 50)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\football\\football.gml", "FOOTBALL", 300, 50)
#
# # MY TESTS
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test1.gml", "CHATGPT", 300, 50)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test2.gml", "LES MISERABLES", 300, 50)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test4.gml", "NEURAL NETWORK", 500, 50)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\polbooks.gml", "POLITICAL BOOKS", 300, 50)
# solver("C:\Proiecte SSD\Python\lab3AI\\networks\\myNetworks\\test6.gml", "WORLD ADJACENCIES", 300, 50)

