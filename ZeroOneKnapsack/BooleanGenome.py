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
from random import randint
from ZOKSInstance import ZOKSInstance

class FitnessMode(Enum):
    Regular = 0
    DeathPenalty = 1
    Penalty = 2
    Repair = 3


class BooleanGenome:

    """
    public BooleanGenome( ZOKSInstance instance ) {
        weight = 0;
        profit = 0;
        this.genes = new boolean[instance.getNItems()];
        for ( int i = 0; i < genes.length; i++ ) {
            if ( Math.random() < 0.5 ) {
                if ( weight + instance.getWeight( i ) <= instance.getCapacity() ) {
                    genes[ i ] = true;
                    weight += instance.getWeight( i );
                    profit += instance.getProfit( i );
                }
            }
        }
        this.instance = instance;
    }
    """
    def __init__(self, instance:ZOKSInstance):
        self._genes = [bool(randint(0, 1)) if True else False for i in range(function.n_variables)]
        self._function = function
        self._fitness = None
        self._is_changed = True


    """
    public BooleanGenome(BooleanGenome g) {
        genes = Arrays.copyOf( g.genes, g.genes.length);
        function = g.function;
    }
    """
    @classmethod
    def from_BooleanGenome(cls, g:BooleanGenome):
        ng = cls(g._function)
        ng._genes = g._genes[:] # This will copy all elements and create a new list
        ng._is_changed = g._is_changed #False
        ng._fitness = g._fitness
        return ng

    """
    public int getSize() {
        return genes.length;
    }
    """
    @property
    def size(self):
        return len(self._genes)

    """
    public boolean getValue() {
        return function.getValue(genes);
    }
    """
    @property
    def value(self):
        return self._function.getValue(self._genes)

    @value.setter
    def value_setter(self, v):
        pass

    # @property
    def get_gene(self, i:int)->bool:
        return self._genes[i]

    # @gene.setter
    def set_gene(self, i:int, value:bool):
        self._genes[i] = value
        self._is_changed = True

    def __len__(self):
        return len(self._genes)

    """
    @Override
    public String toString() {
        String out="";
        for ( boolean gene : genes ) {
            out = out + String.valueOf (gene);
        }
        return out;
    }
    """
    def __str__(self):
        return " ".join([str(gene) for gene in self._genes])

    """
    BooleanGenome getBestNeighbor() {
        for ( int i = 0; i < genes.length; i++ ) {
            BooleanGenome n = new BooleanGenome( this );
            n.flipGene(i);
            if ( n.getValue() ) return n;
        }
        return null;
    }
    """
    def best_neighbor(self)->BooleanGenome:
        best_fitness = 1e10
        best = None

        for i in range(len(self._genes)):
            n = self.from_BooleanGenome(self) #BooleanGenome(self)
            n.flip_gene(i)
            if(n.fitness() < best_fitness):
                best_fitness =  n._fitness
                best = n

        return best

    """
    BooleanGenome getRandomNeighbor() {
        Random r = new Random();
        BooleanGenome n = new BooleanGenome( this );
        n.flipGene( r.nextInt( genes.length ) );
        return n;
    }
    """
    def random_neighbor(self)->BooleanGenome:
        n = BooleanGenome.from_BooleanGenome(self)
        n.flip_gene(randint(0, len(self._genes)-1))
        return n

    """
    BooleanGenome getRandomNeighborNotInTabu( int nTries, List<Integer> tabuList ) {
            int bestNeighborFitness = Integer.MAX_VALUE;
            BooleanGenome best = null;
            Random r = new Random();

            int bestPos = 0;
            for ( int i = 0; i < nTries; i++ ) {
                BooleanGenome n = new BooleanGenome( this );
                int pos;
                while ( true ) {
                    pos = r.nextInt( genes.length );
                    if ( !tabuList.contains( pos ) ) {
                        break;
                    }
                }

                n.flipGene(pos);
                int newfitness = n.getFitness();
                if ( newfitness < bestNeighborFitness ) {
                    bestNeighborFitness = newfitness;
                    best = n;
                    bestPos = pos;
                }

            }
            tabuList.add( bestPos ) ;
            return best;
        }
    }
    """
    def random_neighbor_not_in_tabu(self, nTries:int, tabuList:List)->BooleanGenome:
        best_neighbor_fitness = 1e10
        best = None

        best_pos = 0
        for i in range(nTries):
            n = BooleanGenome.from_BooleanGenome(self)
            pos = 0
            while True:
                pos = randint(0, len(self._genes)-1)
                if pos not in tabuList:
                    break
            
            n.flip_gene(pos)
            new_fitness = n.fitness()
            if(new_fitness < best_neighbor_fitness):
                best_neighbor_fitness = new_fitness
                best = n
                best_pos = pos

        tabuList.append(best_pos)
        return best

    """
    private void flipGene( int i ) {
        genes[i]=!genes[i];
    }
    """
    def flip_gene(self, index:int):
        self._genes[index] = not self._genes[index]
        self._is_changed = True

    """
    int getFitness() {
        if ( changed ) {
            fitness = 0;
            for ( int i = 0; i < function.getnClauses(); i++ ) {
                if ( !function.getClauseValue( i, genes ) ) {
                    fitness++;
                }
            }
        }
        return fitness;
    }
    """
    def fitness(self):
        if(self._is_changed):
            self._fitness = 0
            for i in range(self._function.n_clauses):
                if(not self._function.clause_value(i, self._genes)):
                    self._fitness += 1
        
        return self._fitness

    """
    boolean isSatisfied() {
        return getFitness() == 0;
    }
    """
    def is_satisfied(self)->bool:
        return self._fitness == 0



