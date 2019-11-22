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
from random import randint, random
from ZOKSInstance import ZOKSInstance

class FitnessMode(Enum):
    Regular = 0
    DeathPenalty = 1
    Penalty = 2
    Repair = 3


class BooleanGenome:

    fitness_mode:FitnessMode = FitnessMode.Regular
    penalty_value:int = 10

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
        self._weight:int = 0
        self._profit:int = 0
        self._genes:List[bool] = [False for i in range(instance.n)]
        for i in range(len(self._genes)):
            if(random() < 0.5):
                if(self._weight + instance.weight[i] <= instance.capacity):
                    self._genes[i] = True
                    self._weight += instance.weight[i]
                    self._profit += instance.profit[i]
                    
        self._instance = instance
        self._is_changed = False


    """
    public BooleanGenome( BooleanGenome g ) {
        genes = Arrays.copyOf( g.genes, g.genes.length );
        instance = g.instance;
        changed = g.changed;
        profit = g.profit;
    }
    """
    @classmethod
    def from_BooleanGenome(cls, g:BooleanGenome):
        ng = cls(g._instance)
        ng._genes = g._genes[:] # This will copy all elements and create a new list
        # ng._instance = g._instance
        ng._is_changed = g._is_changed #False
        ng._profit = g._profit
        return ng

    @property
    def weight(self)->int:
        return self._weight

    # def __len__(self):
    #     return len(self._genes)

    def get_gene(self, i:int)->bool:
        return self._genes[i]

    def set_gene(self, i:int, value:bool):
        self._genes[i] = value
        self._is_changed = True

    # """
    # public int getSize() {
    #     return genes.length;
    # }
    # """
    # @property
    # def size(self):
    #     return len(self._genes)

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
            profit = 0;
            weight = 0;
            for ( int i = 0; i < instance.getNItems(); i++ ) {
                if ( getGene( i ) ) {
                    profit += instance.getProfit( i );
                    weight += instance.getWeight( i );
                }
            }
        }

        if ( weight > instance.getCapacity() ) { //infeasible
            if ( fitnessMode == FitnessMode.Regular ) {
                return profit;
            }
            if ( fitnessMode == FitnessMode.DeathPenalty ) {
                return Integer.MIN_VALUE;
            }
            if ( fitnessMode == FitnessMode.Penalty ) {
                return profit - (weight - instance.getCapacity()) * penaltyValue;
            }
            if ( fitnessMode == FitnessMode.Repair ) {
                Random rnd = new Random();
                while ( weight > instance.getCapacity() ) { //remove a random item
                    int index = rnd.nextInt( genes.length );
                    if ( getGene( index )) {
                        genes[ index ] = false;
                        weight -= instance.getWeight( index );
                        profit -= instance.getProfit(index );
                    }
                }
            }         
        }
        return profit;

    }
    """
    def fitness(self)->int:
        if(self._is_changed):
            self._profit = 0
            self._weight = 0
            for i in range(self._instance.n):
                if(self.get_gene(i)):
                    self._profit += self._instance.profit[i]
                    self._weight += self._instance.weight[i]

        if(self._weight > self._instance.capacity):
            if(self.fitness_mode == FitnessMode.Regular):
                return self._profit

            if(self.fitness_mode == FitnessMode.DeathPenalty):
                return -1e10

            if(self.fitness_mode == FitnessMode.Penalty):
                return self._profit - (self._weight - self._instance.capacity)*self.penalty_value

            if(self.fitness_mode == FitnessMode.Repair):
                while(self._weight > self._instance.capacity):
                    index:int = randint(0, len(self._genes)-1)
                    if(self.get_gene(index)):
                        self._genes[index] = False
                        self._weight -= self._instance.weight[index]
                        self._profit -= self._instance.profit[index]
        
        return self._profit

    """
    public boolean isFeasible() {
        getFitness();
        return weight <= instance.getCapacity();
    }
    """
    def is_feasible(self)->bool:
        self.fitness()
        return self._weight <= self._instance.capacity

    """
    public boolean isBetter( BooleanGenome rhs ) {
        if ( this.isFeasible() && rhs.isFeasible() ) {
            return profit > rhs.profit;
        }
        if ( !this.isFeasible() && !rhs.isFeasible() ) {
            return (weight - instance.getCapacity()) < (rhs.weight - instance.getCapacity());
        }

        return this.isFeasible();
    }
    """
    def is_better(self, rhs:BooleanGenome)->bool:
        if(self.is_feasible() and rhs.is_feasible()):
            return self._profit > rhs._profit
        if(not self.is_feasible() and not rhs.is_feasible()):
            return (self.weight - self._instance.capacity) < (rhs.weight - self._instance.capacity)
