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

from typing import List

class ZOKSInstance:
    
    def __init__(self, problem_name:str):
        self._n = 0
        self._capacity = 0
        self._profit = [int]
        self._weight = [int]

    def read_data(self, problem_name:str):
        try:
            with open(problem_name, "r") as data_file:
                data_lines:List[str] = data_file.readlines()

                _n, _capacity = data_lines[0].split()
                _profit, _weight = [int], [int]

                for data_line in range(data_lines[1:]):
                    line_profit, line_capacity = data_line.split()
                    _profit.append(line_profit)
                    _weight.append(line_capacity)
        except FileNotFoundError:
            print("File cannot be opened.")
        
    
    @property
    def n(self)->int:
        return self._n

    @n.setter
    def n(self, value):
        pass

    @property
    def capacity(self)->int:
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        pass

    @property
    def profit(self)->List[int]:
        return self._profit

    @profit.setter
    def profit(self, value):
        pass

    @property
    def weight(self)->List[int]:
        return self._weight

    @weight.setter
    def weight(self, value):
        pass


