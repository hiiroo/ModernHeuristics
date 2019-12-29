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

from typing import List
from functools import cmp_to_key
from Genome import Genome


class Population():


    def __init__(self):
        self._population:List[Genome] = []


    def add_genome(self, g:Genome):
        self._population.append(g)


    @property
    def population(self)->List[Genome]:
        return self._population


    def get_genome(self, i:int)->Genome:
        return self._population[i]

    def remove_genome(self, i:int):
        self._population.remove(self._population[i])


    def sort(self, fitness_comparator):
        sorted(self._population, key=cmp_to_key(fitness_comparator))

    
    def __len__(self):
        return len(self._population)

    def __str__(self):
        popstr = []
        for genome in self.population:
            popstr.append(str(genome))

        return "\n".join(popstr)
    
    def __contains__(self, g:Genome):
        for genome in self.population:
            if(genome.nobjectives == g.nobjectives and genome.nvariables == g.nvariables):
                return True
        return False


    