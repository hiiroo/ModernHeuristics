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
from BooleanGenome import BooleanFunction

class CNFFunction(BooleanFunction):

    def __init__(self, problem_name:str, *args, **kwargs):
        super.__init__(args, kwargs)
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
        self.clauses = []

        try:
            with open(problem_name, "r") as input:
                lines = input.readlines()
                
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
                        self.clauses.append(new_clause)
                if(len(self.clauses) != len(self.__n_clauses)):
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

        for j in range(len(self.__clauses)):
            variable = clause[i]
            if(variable < 0):
                value = value or (not genes[-variable-1])
            else:
                value = value or (genes[-variable-1])
        
        return value
