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
from Comparators import compare_dominance
from Population import Population

class NonDominatedPopulation(Population):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_genome(self, g):
        i:int = 0
        while i < len(self):
            result = compare_dominance(self.get_genome(i), g)

            if(result == -1): # It has dominated by a genome from the population
                return

            if(result == 1): # It has dominated a genome from the population
                super().remove_genome(i)
                i-=1
            i+=1
        
        return super().add_genome(g)

    def __str__(self):
        return super().__str__()