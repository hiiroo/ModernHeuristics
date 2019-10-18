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
    def from_permutation(cls, permutation:str, instance:TSPInstance):
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
    def from_instance(cls, n:int, instance:TSPInstance):
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
    def from_genome(cls, n):
        pg = cls()
        pg._chromosome = deepcopy(n.chromosome)
        pg._instance = n.instance
        return pg


    @property 
    def chromosome(self):
        return self._chromosome

    @chromosome.setter
    def chromosome_setter(self, v):
        pass


    @property
    def instance(self):
        return self._instance

    @instance.setter
    def instance_setter(self, v):
        pass


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
    def fitness(self):
        return sum([self._instance.distance[self._chromosome.gene(i)][self._chromosome.gene(i+1)] for i in range(len(self.chromosome)-1)])


    """
    private void swapGenes( int i, int j ) {
        chromosome.swapGenes(i,j);
    }
    """
    def swap_genes(self, i:int, j:int):
        self._chromosome.swap_genes(i, j)


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
    def best_neighbor(self):
        best_fitness = 1e10
        best = None

        for i in range(len(self._chromosome)-1):
            for j in range(len(self._chromosome)):
                n = PermutationGenome.from_genome(self)
                n.swap_genes(i, j)
                newfitness = n.fitness()
                if(newfitness < best_fitness):
                    best_fitness = newfitness
                    best = n
        
        return best
