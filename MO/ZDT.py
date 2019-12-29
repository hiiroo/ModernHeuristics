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
from math import sqrt
from Genome import Genome

class ZDTOne:

    def values(self, genome:Genome)->List[float]:
        objectives:List[float] = [.0 for i in range(genome.nobjectives)]
        objectives[0] = genome.variable(0)

        sumv:float = 0
        for i in range(genome.nvariables):
            sumv+=genome.variable(i)
        g = 1 + (9.0 / (genome.nvariables -1)) * sumv
        objectives[1] = g*(1-sqrt(objectives[0]/g))

        return objectives
