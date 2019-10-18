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

from random import randint

class BooleanFunction:

    @staticmethod
    def getValue(genes:list):
        return ( genes[0] or not genes[1] or not genes[2] ) and\
               ( not genes[0] or not genes[1] or not genes[2] ) and\
               ( genes[1] or genes[2] ) and ( genes[2] or genes[3] ) and\
               ( genes[2] or not genes[3] )


class BooleanGenome:

    """
    public BooleanGenome( int n, BooleanFunction function ) {
        this.genes = new boolean[n];
        for ( int i = 0; i < genes.length; i++ ) {
            if( Math.random() < 0.5)
                genes[i]=true;
        }
        this.function = function;
    }

    """
    def __init__(self, n, function:BooleanFunction):
        self._genes = [bool(randint(0, 1)) if True else False for i in range(n)]
        self._function = function


    """
    public BooleanGenome(BooleanGenome g) {
        genes = Arrays.copyOf( g.genes, g.genes.length);
        function = g.function;
    }
    """
    @classmethod
    def from_BooleanGenome(cls, g):
        ng = cls(len(g._genes), g._function)
        ng._genes = g._genes[:] # This will copy all elements and create a new list
        return ng


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
    def best_neighbor(self):
        for i in range(len(self._genes)):
            n = self.from_BooleanGenome(self) #BooleanGenome(self)
            n.flip_gene(i)
            if n.value :
                return n

    """
    private void flipGene( int i ) {
        genes[i]=!genes[i];
    }
    """
    def flip_gene(self, i:int):
        self._genes[i] = not self._genes[i]

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
