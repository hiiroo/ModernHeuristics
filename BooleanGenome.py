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
from random import randint

class BooleanFunction:

    @staticmethod
    def getValue(genes:list):
        return ( genes[0] or not genes[1] or not genes[2] ) and\
               ( not genes[0] or not genes[1] or not genes[2] ) and\
               ( genes[1] or genes[2] ) and ( genes[2] or genes[3] ) and\
               ( genes[2] or not genes[3] )


class CNFFunction(BooleanFunction):

    def __init__(self, problem_name:str, *args, **kwargs):
        # super().__init__(args, kwargs)
        self.__n_variables = None
        self.__n_clauses = None
        self.__clauses = []
        self.__read_instance(problem_name)
        
    """
    public int getnClauses() {
        return nClauses;
    }
    """
    @property
    def n_clauses(self)->int:
        return self.__n_clauses

    @n_clauses.setter
    def n_clauses(self, value:int):
        pass

    """
    public int getnVariables() {
        return nVariables;
    }
    """
    @property
    def n_variables(self)->int:
        return self.__n_variables

    @n_variables.setter
    def n_variables(self, value:int):
        pass

    """
    private void readInstance( String problemName ) {
        clauses = new ArrayList<>();
        try ( Scanner input = new Scanner( new File( problemName ) ) ) {
            while ( input.hasNext() ) {
                String line = input.nextLine();

                if ( line.startsWith( "c" ) ) {
                    continue; //skip comment lines
                }
                if ( line.startsWith( "p" ) ) {//read nVariables and nClauses
                    String[] tokens = line.split( " " );
                    nVariables = Integer.parseInt( tokens[ 2 ] );
                    nClauses = Integer.parseInt( tokens[ 3 ] );
                }
                else { //read clauses
                    String[] tokens = line.split( " " );
                    List<Integer> newClause = new ArrayList();
                    for ( int i = 0; i < tokens.length - 1; i++ ) {
                        newClause.add( Integer.parseInt( tokens[ i ] ) );
                    }
                    clauses.add( newClause );
                }
            }
            input.close();
            if ( clauses.size() != nClauses ) {
                System.out.println( "Possible problem in CNF file" );
            }
        } catch ( FileNotFoundException ex ) {
            System.out.println( "File cannot be openned." );
        }
    }
    """
    def __read_instance(self, problem_name:str):
        self.__clauses = []

        try:
            with open(problem_name, "r") as input_file:
                lines = input_file.readlines()
                
                for line in lines:
                    if(line.startswith("c")):
                        continue

                    if(line.startswith("p")):
                        tokens = line.split()
                        self.__n_variables = int(tokens[2])
                        self.__n_clauses = int(tokens[3])
                    else:
                        tokens = line.split()
                        new_clause = []
                        for i in range(len(tokens)-1):
                            new_clause.append(int(tokens[i]))
                        self.__clauses.append(new_clause)
                if(len(self.__clauses) != self.__n_clauses):
                    print("Possible problem in CNF file.")
        except FileNotFoundError:
            print("File cannot be opened.")

    """
    boolean getClauseValue( int i, boolean[] genes ) {
        List<Integer> clause = clauses.get( i );
        boolean value = false;
        for ( int j = 0; j < clause.size(); j++ ) {
            int variable = clause.get( j );
            if ( variable < 0 ) {
                value = value || !genes[ -variable - 1 ];
            }
            else {
                value = value || genes[ variable - 1 ];
            }
        }
        return value;
    }
    """
    def clause_value(self, i:int, genes:List[bool])->bool:
        clause = self.__clauses[i]
        value = False

        for j in range(len(clause)):
            variable = clause[j]
            if(variable < 0):
                value = value or (not genes[-variable-1])
            else:
                value = value or (genes[variable-1])
        
        return value



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
    def __init__(self, function:CNFFunction):
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
        ng._is_changed = False
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
    def flip_gene(self, i:int):
        self._genes[i] = not self._genes[i]
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



