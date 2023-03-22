import random
from random import randint

from utils.utils import generateNewValue


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        # self.__repres = [generateNewValue(problParam['min'], problParam['max']) for _ in range(problParam['noDim'])]
        # self.__fitness = 0.0

        self.repres = [generateNewValue(0, problParam['noNodes']) for _ in range(problParam['noNodes'])]
        self.fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        r = randint(0, len(self.__repres) - 1)
        val = self.repres[r]
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i])
            #newrepres.append(val)
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring


    def mutation(self):
        pos = randint(0, len(self.__repres) - 1)
        #self.__repres[pos] = generateNewValue(0, max(self.__repres))
        self.__repres[pos] = random.sample(set(self.repres), 1)[0] # nu pot adauga o comunitate noua / pot doar sa integrez nodul intr-o alta com

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

    def __lt__(self, other):
        return self.fitness > other.fitness # cromozomul cu fitness mai mare va fi considerat cel mai mic ( util pentru heapify = min heap)