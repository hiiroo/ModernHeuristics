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
from typing import Dict
from random import randint
from copy import deepcopy
from TSPInstance import TSPInstance
from PermutationType import PermutationType

class PermutationGenome:

    """
    I had to make some design changes.
    public PermutationGenome( String permutation, TSPInstance instance ) {
        chromosome = new PermutationType( permutation );
        this.instance = instance;
        this.instance.readData();
    }
    """
    def __init__(self):
        self._chromosome = None #PermutationType(permutation)
        self._instance = None #instance
        # self._instance.read_data()


    @classmethod
    def from_permutation(cls, permutation:str, instance:TSPInstance)->PermutationGenome:
        pg = cls()
        pg._chromosome = PermutationType(permutation)
        pg._instance = instance
        return pg


    """
    PermutationGenome(int n, TSPInstance instance) {
        chromosome = new PermutationType(n);
        this.instance = instance;
    }
    """
    @classmethod
    def from_instance(cls, n:int, instance:TSPInstance)->PermutationGenome:
        pg = cls()
        pg._chromosome = PermutationType.from_random(n)
        pg._instance = instance
        return pg


    """
    PermutationGenome(PermutationGenome n) {
        this.instance = n.instance;
        this.chromosome = new PermutationType(n.chromosome );
    }
    """
    @classmethod
    def from_genome(cls, n:PermutationGenome)->PermutationGenome:
        pg = cls()
        pg._chromosome = deepcopy(n.chromosome)
        pg._instance = n.instance
        return pg


    @property 
    def chromosome(self)->PermutationType:
        return self._chromosome

    @chromosome.setter
    def chromosome_setter(self, v):
        pass


    @property
    def instance(self)->TSPInstance:
        return self._instance

    @instance.setter
    def instance_setter(self, v):
        pass

    def __str__(self):
        return str(self.chromosome)

    """
    int getFitness() {
        int distance = 0;
        for ( int i = 0; i < chromosome.size(); i++ ) {
            distance += instance.getDistance( chromosome.getGene( i ),
                    chromosome.getGene( (i + 1) % chromosome.size() ) );
        }
        return distance;
    }
    """
    def fitness(self)->float:
        return sum([self.instance.distance[self.chromosome.gene(i)][self.chromosome.gene(i+1)] for i in range(len(self.chromosome)-1)])


    """
    private void swapGenes( int i, int j ) {
        chromosome.swapGenes(i,j);
    }
    """
    def swap_genes(self, i:int, j:int):
        self.chromosome.swap_genes(i, j)


    """
    public void twoOpt() {
        boolean modified = true;
        while (modified) {
            modified = false;

            for (int i = 0; i < chromosome.size() - 2; i++) {
                for (int j = i + 2; j < chromosome.size() - 1; j++) {
                    int d1 = getDistanceBetween(i, i + 1)
                            + getDistanceBetween(j, j + 1);
                    int d2 = getDistanceBetween(i, j)
                            + getDistanceBetween(i + 1, j + 1);

                    // if distance can be shortened, adjust the tour
                    if (d2 < d1) {
                        chromosome.reverse(i + 1, j);
                        modified = true;
                    }
                }
            }
        }
    }
    """
    def two_opt(self):
        modified = True
        while(modified):
            modified = False

            for i in range(len(self.chromosome)-2):
                for j in range(len(self.chromosome)-1):
                    d1 = self.distance(self.chromosome.gene(i), self.chromosome.gene(i+1)) + self.distance(self.chromosome.gene(j), self.chromosome.gene(j+1))
                    d2 = self.distance(self.chromosome.gene(i), self.chromosome.gene(j)) + self.distance(self.chromosome.gene(i+1), self.chromosome.gene(j+1))

                    if(d2 < d1):
                        self.chromosome.reverse(d1, d2)
                        

    """
    private int getDistanceBetween(int pos1, int pos2) {
        return instance.getDistance(chromosome.getGene(pos1),
                chromosome.getGene(pos2));
    }
    """
    def distance(self, pos1:int, pos2:int):
        return self.instance.distance[pos1][pos2]


    """
    PermutationGenome getBestNeighbor() {
        int bestFitness = Integer.MAX_VALUE;
        PermutationGenome best = null; 
        for ( int i = 0; i < chromosome.size()-1; i++ ) {
            for ( int j = i + 1; j < chromosome.size(); j++ ) {
                PermutationGenome n = new PermutationGenome(this);
                n.swapGenes(i,j);
                int newfitness = n.getFitness();
                if ( newfitness < bestFitness) {
                    bestFitness = newfitness;
                    best = n;
                }
            }
            
        }
        return best;
    }
    """
    def best_neighbor(self, tabulist:list=[]):
        best_fitness = 1e10
        best = None

        for i in range(len(self.chromosome)-1):
            for j in range(len(self.chromosome)):
                n = PermutationGenome.from_genome(self)
                n.swap_genes(i, j)
                newfitness = n.fitness()
                if(newfitness < best_fitness and newfitness not in tabulist):#Why do we check fitness as tabu? 
                    best_fitness = newfitness
                    best = n
        
        return best


    """
    PermutationGenome getRandomNeighbor() {
        Random r = new Random();
        PermutationGenome n = new PermutationGenome(this);
        n.swapGenes(r.nextInt(chromosome.size()), r.nextInt(chromosome.size()));
        return n;
    }
    """
    def random_neighbor(self):
        n = PermutationGenome.from_genome(self)
        n.swap_genes(randint(0, len(self.chromosome)-1), randint(0, len(self.chromosome)-1))
        return n


    """
    PermutationGenome getRandomNeighborNotInTabu( int nTries, List<AbstractMap.SimpleEntry<Integer, Integer>> tabuList ) {
        int bestNeighborFitness = Integer.MAX_VALUE;
        PermutationGenome best = null;
        Random r = new Random();

        int bestPos1 = 0, bestPos2 = 0;
        for ( int i = 0; i < nTries; i++ ) {
            PermutationGenome n = new PermutationGenome( this );
            int pos1, pos2;
            while ( true ) {
                pos1 = r.nextInt( chromosome.size() );
                pos2 = r.nextInt( chromosome.size() );
                AbstractMap.SimpleEntry<Integer, Integer> item = new AbstractMap.SimpleEntry( pos1, pos2 );
                if ( !tabuList.contains( item ) ) {
                    break;
                }
            }

            n.swapGenes( pos1, pos2 );
            int newfitness = n.getFitness();
            if ( newfitness < bestNeighborFitness ) {
                bestNeighborFitness = newfitness;
                best = n;
                bestPos1 = pos1;
                bestPos2 = pos2;
            }

        }
        tabuList.add( new AbstractMap.SimpleEntry( bestPos1, bestPos2 ) );
        return best;
    }
    """
    def random_neighbor_not_in_tabu(self, nTries:int, tabuList:Dict)->PermutationGenome:
        best_neighbor_fitness = 1e10
        best = None

        best_pos_1, best_pos_2 = 0, 0
        for i in range(nTries):
            n = PermutationGenome.from_genome(self)
            pos1, pos2 = 0, 0
            while True:
                pos1 = randint(0, len(self.chromosome))
                pos2 = randint(0, len(self.chromosome))
                if pos1 not in tabuList:
                    break
            
            n.swap_genes(pos1, pos2)
            new_fitness = n.fitness()
            if(new_fitness < best_neighbor_fitness):
                best_neighbor_fitness = new_fitness
                best = n
                best_pos_1 = pos1
                best_pos_2 = pos2

        tabuList[best_pos_1] = best_pos_2
        return best


