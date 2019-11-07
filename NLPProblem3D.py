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
from math import inf

"""
3D problem from https://www.wikiwand.com/en/Nonlinear_programming
"""
class NLPProblem3D:

    @property
    def dimension(self):
        3

    @dimension.setter
    def dimension_setter(self):
        pass

    def value(self, vars:List[float]):
        if(self.is_valid(vars)):
            return vars[0]*vars[1] + vars[1]*vars[2]

        return inf

    def is_valid(self, vars:List[float]):
        sum = vars[0]**2 - vars[1]**2 + vars[2]**2
        if(sum < 2):
            return False

        squared_sum = sum(map(lambda x: x**2, vars)) #vars[0]**2 + vars[1]**2 + vars[2]**2

        if(squared_sum > 10):
            return False

        return True
        