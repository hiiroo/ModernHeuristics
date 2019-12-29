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

from random import randint, random
from tqdm import tqdm
from zdt import ZDTOne
from Genome import Genome
from NonDominatedPopulation import NonDominatedPopulation
from NonDominatingSortingPopulation import NonDominatingSortingPopulation

class NSGAII:

    def __init__(self):
        self._population:NonDominatedPopulation

    def run(self, ngeneration:int, populationsize:int, crossoverrate:float, mutationrate:float, problem:ZDTOne):
        self._population = NonDominatingSortingPopulation()
        for generationcount in range(populationsize):
            gene:Genome = Genome(2, 2)
            gene.calculate_fitnesses(problem)
            self._population.add_genome(gene)

        self._population.rank()

        for generationcount in tqdm(range(ngeneration)):
            for nchildren in range(populationsize):
                parent1:Genome = self.tournament_selection(populationsize)
                parent2:Genome = self.tournament_selection(populationsize)

                rand = random()

                if(rand < crossoverrate):
                    self.crossover(parent1, parent2)
                else:
                    self._population.add_genome(parent1)
                    self._population.add_genome(parent2)

                if(random() < mutationrate):
                    self.mutate(self._population.get_genome(-1))
                    self.mutate(self._population.get_genome(-2))
                
                self._population.get_genome(-1).calculate_fitnesses(problem)
                self._population.get_genome(-2).calculate_fitnesses(problem)

            self._population.rank()
            self._population.truncate(populationsize)
    
        return self._population


    def tournament_selection(self, population_size:int)->Genome:
        g1:Genome = self._population.get_genome(randint(0, population_size-1))
        g2:Genome = self._population.get_genome(randint(0, population_size-1))

        if(g1.rank < g2.rank):
            return g1

        if(g2.rank < g1.rank):
            return g2

        if(g1.crowding_distance > g2.crowding_distance):
            return g1

        return g2


    def crossover(self, parent1:Genome, parent2:Genome)->Genome:
        child1:Genome = Genome(2, 2)
        child2:Genome = Genome(2, 2)

        for i in range(parent1.nvariables):
            if(random() < 0.5):
                child1.variable(i, parent1.variable(i))
                child2.variable(i, parent2.variable(i))
            else:
                child1.variable(i, parent2.variable(i))
                child2.variable(i, parent1.variable(i))
        self._population.add_genome(child1)
        self._population.add_genome(child2)

    def mutate(self, genome:Genome):
        for i in range(genome.nvariables):
            val = random()
            if(random() < 0.5):
                # val = -val
                genome.variable(i, val)
