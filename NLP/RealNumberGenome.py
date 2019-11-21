"""
MIT License

Copyright (c) 2019 Ali Mert Ceylan, Adopted from original resources provided
by Korhan Karabulut for COMP 5658 Modern Heuristics Course

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations
from typing import List
from copy import copy
from math import inf
from random import random
from NLPProblem3D import NLPProblem3D

class RealNumberGenome:

    def __init__(self):
        self._genes = None
        self._instance = None


    @classmethod
    def from_instance(cls, instance:NLPProblem3D)->RealNumberGenome:
        genes = [0 for i in range(instance.dimension)]
        for i in range(len(genes)):
            multiplier = 1
            if(random() < 0.5):
                multiplier = -1
            genes[i] = multiplier * random()
        
        rng = cls()
        rng._genes = genes
        rng._instance = instance
        return rng
        

    @classmethod
    def from_genome(cls, g:RealNumberGenome)->RealNumberGenome:
        rng = cls()
        rng._genes = copy(g._genes)
        rng._instance = g._instance
        return rng

    @property 
    def genes(self)->List[float]:
        return self._genes

    @genes.setter
    def genes(self, value:List[float]):
        pass

    @property
    def instance(self)->NLPProblem3D:
        return self._instance

    @instance.setter
    def instance(self, value:NLPProblem3D):
        pass
    
    def fitness(self)->float:
        return self.instance.value(self.genes)

    
    def best_neighbor(self, epsilon:float)->RealNumberGenome:
        best_fitness = -inf
        best = None

        for i in range(len(self.genes)):
            n1 = RealNumberGenome.from_genome(self)
            n1.mutate_gene(i, epsilon)

            n2 = RealNumberGenome.from_genome(self)
            n2.mutate_gene(i, -epsilon)

            if(n1.fitness() > best_fitness):
                best = n1
                best_fitness = n1.fitness()

            if(n2.fitness() > best_fitness):
                best = n2
                best_fitness = n2.fitness()

        return best


    def mutate_gene(self, gene:int, epsilon:float):
        self.genes[gene] += epsilon


    def __str__(self):
        return " ".join(["{:6.6f}".format(g) for g in self.genes])
