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

from random import shuffle, randint

class PermutationType:

    """
    public PermutationType( int[] permutation ) {
        this.permutation = permutation;
    }
    """
    def __init__(self, permutation:list):
        self._permutation = permutation


    @property
    def permutation(self):
        return self._permutation #If permutation should not be accessed anyway, it can be replaced by a pass

    @permutation.setter
    def permutation_setter(self, v):
        pass


    """
    public PermutationType( String permutation ) {
        String numbers[] = permutation.split( " ");
        this.permutation = new int [numbers.length];
        for ( int i = 0; i < numbers.length; i++ ) {
            this.permutation[i]=Integer.parseInt( numbers[i] )-1;
        }
    }
    """
    @classmethod
    def from_string(cls, permutation:str):
        numbers = permutation.split()
        return cls([int(number)-1 for number in numbers])


    """
    PermutationType(int n ) {
        permutation=new int [n];
        for ( int i = 0; i < permutation.length; i++ ) {
            permutation[ i ] = i;            
        }
        Random r = new Random();
        for ( int i = 0; i < permutation.length; i++ ) {
            int p1 = r.nextInt( permutation.length );
            int p2 = r.nextInt( permutation.length );
            int temp = permutation[p1];
            permutation[p1] = permutation[p2];
            permutation[p2]=temp;
        }                
    }
    """
    @classmethod
    def from_random(cls, n):
        l = [i for i in range(n)]
        for i in range(n):
            p1 = randint(0, n-1)
            p2 = randint(0, n-1)
            l[p1], l[p2] = l[p2], l[p1]
        return cls(l)


    """
    PermutationType( PermutationType chromosome ) {
        this.permutation=Arrays.copyOf( chromosome.permutation, chromosome.permutation.length );
    }
    """
    @classmethod
    def from_chromosome(cls, chromosome):
        return cls(list(chromosome))


    """
    int getGene(int index) {
        return permutation[index];
    }
    """
    def gene(self, index):
        return self._permutation[index]


    """
    int size() {
        return permutation.length;
    }

    Additionally it overrides __len__ function of object class
    and length of permutation genome can be obtained by len function directy.
    """
    def __len__(self):
        return len(self._permutation)


    """
    void swapGenes( int i, int j ) {
        int temp = permutation[i];
        permutation[i] = permutation[j];
        permutation[j] = temp;
    }
    """
    def swap_genes(self, i, j):
        self._permutation[i], self._permutation[j] = self._permutation[j], self._permutation[i]