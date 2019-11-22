"""
MIT License

Copyright (c) 2019 Ali Mert Ceylan, Adopted from original resources provided 
by Korhan Karabulut for COMP 5658 Modern Heuristics Graduate Course

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
from enum import Enum
from random import randint, random, shuffle
from tqdm import tqdm
from ZOKSInstance import ZOKSInstance
from BooleanGenome import BooleanGenome

class TournamentType(Enum):
    FITNESS = 0
    SoF = 1


class ZOKSGA:

    def __init__(self):
        self.population: List[BooleanGenome] = []

    """
    private List<BooleanGenome> tournamentSelection( int tournamentSize, int populationSize, TournamentType tournamentType ) {
        List<BooleanGenome> matingPool = new ArrayList<>();
        Random r = new Random();
        for ( int i = 0; i < populationSize; i++ ) {
            int index = r.nextInt( tournamentSize );
            BooleanGenome bestCandidate = population.get( index );
            for ( int j = 0; j < tournamentSize - 1; j++ ) {
                index = r.nextInt( tournamentSize );
                BooleanGenome curr = population.get( index );
                if ( tournamentType == TournamentType.SoF ) {
                    if ( curr.isBetter( bestCandidate ) ) {
                        bestCandidate = curr;
                    }
                }
                else if ( curr.getFitness() > bestCandidate.getFitness() ) {
                    bestCandidate = curr;
                }
            }
            matingPool.add( bestCandidate );
        }
        return matingPool;
    }
    """
    def tournament_selection(self, tournament_size: int, population_size: int, tournamet_type:TournamentType) -> List[BooleanGenome]:
        mating_pool: List[BooleanGenome] = []

        for i in range(population_size):
            index = randint(0, tournament_size)
            best_candidate = self.population[index]
            
            for j in range(tournament_size-1):
                index = randint(0, tournament_size)
                curr = self.population[index]
                if(tournamet_type == TournamentType.SoF):
                    if(curr.is_better(best_candidate)):
                        best_candidate = curr
                elif(curr.fitness() > best_candidate.fitness()):
                    best_candidate = curr

            mating_pool.append(best_candidate)

        return mating_pool

    """
    private void crossover( BooleanGenome parent1, BooleanGenome parent2, List<BooleanGenome> population ) {
        Random r = new Random();
        int crossOverPoint = r.nextInt( parent1.getSize() - 1 );
        BooleanGenome child1 = new BooleanGenome( parent1 );
        for ( int i = crossOverPoint + 1; i < parent1.getSize(); i++ ) {
            child1.setGene( i, parent2.getGene( i ) );
        }
        BooleanGenome child2 = new BooleanGenome( parent2 );
        for ( int i = crossOverPoint + 1; i < parent1.getSize(); i++ ) {
            child2.setGene( i, parent1.getGene( i ) );
        }
        population.add( child1 );
        population.add( child2 );
    }
    """

    def crossover(self, parent1: BooleanGenome, parent2: BooleanGenome, population: List[BooleanGenome]):
        crossover_point = randint(0, len(parent1)-1)
        child1 = BooleanGenome.from_BooleanGenome(parent1)

        for i in range(crossover_point+1, len(parent1)):
            child1.set_gene(i=i, value=parent2.get_gene(i))

        child2 = BooleanGenome.from_BooleanGenome(parent2)

        for i in range(crossover_point+1, len(parent2)):
            child2.set_gene(i=i, value=parent1.get_gene(i))

        population.append(child1)
        population.append(child2)


    def run(self, n_generations: int, population_size: int, crossover_rate: float, mutation_rate: float, instance:ZOKSInstance, tournament_type:TournamentType):
        self.population: List[BooleanGenome] = []

        for i in range(population_size):
            gene = BooleanGenome(instance)
            self.population.append(gene)

        best:BooleanGenome = self.population[0]
        for pop_gene in self.population:
            if(pop_gene.fitness() < best.fitness()):
                best = BooleanGenome.from_BooleanGenome(pop_gene)

        for i in tqdm(range(n_generations)):
            mating_pool = self.tournament_selection(10, population_size, tournament_type)

            shuffle(mating_pool)
            self.population.clear()
            # crossover
            for pool_count in range(0, len(mating_pool), 2):
                rand = random()
                if(rand < crossover_rate):
                    self.crossover(
                        mating_pool[pool_count], mating_pool[pool_count + 1], self.population)
                else:
                    self.population.append(mating_pool[pool_count])
                    self.population.append(mating_pool[pool_count + 1])
            # mutation
            for pop_count in range(len(mating_pool)):
                for gene_count in range(instance.n):
                    if(random() < mutation_rate):
                        self.population[pop_count].flip_gene(gene_count)

            for pop_count in range(len(self.population)):
                if(self.population[pop_count].is_better(best)):
                    best = BooleanGenome.from_BooleanGenome(self.population[pop_count])

            del self.population[randint(0, len(self.population)-1)]
            self.population.append(best)

            if(best.fitness() == 0):
                break

        print("ZeroOneKnapsack in GA")
        print(best.fitness())
        print(best)
