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

from tqdm import tqdm
from BooleanGenome import BooleanGenome, CNFFunction
from random import random
from math import exp

class SATTS:

    """
    public void run( int tMax, CNFFunction instance, int maxTabuSize ) {
        long startTime=System.currentTimeMillis();
        BooleanGenome vc = new BooleanGenome( instance );
        List<Integer> tabuList = new ArrayList<>();
        BooleanGenome best = vc;
        int bestFitness = vc.getFitness();

        for ( int t = 0; t < tMax; t++ ) {
            BooleanGenome bestNeighbor = vc.getRandomNeighborNotInTabu(50,tabuList);

            vc = bestNeighbor;
            if ( vc.getFitness() < bestFitness ) {
                bestFitness = vc.getFitness();
                best = vc;
                if ( bestFitness==0) break;
            }
            if ( tabuList.size() > maxTabuSize ) {
                tabuList.remove( 0 );
            }
        }
        long elapsedTime = System.currentTimeMillis() - startTime;
        System.out.println( "\nTabu Search ran for " + elapsedTime + " milliseconds" );
        System.out.println( "Best Fitness: " + bestFitness );
        System.out.println( best );
    }
    """    
    @staticmethod
    def run(tMax:int, instance:CNFFunction, max_tabu_size):
        vc = BooleanGenome(instance)
        tabu_list = []
        best = vc
        best_fitness = vc.fitness()

        for t in tqdm(range(tMax)):
            best_neighbor = vc.random_neighbor_not_in_tabu(50, tabu_list)
            vc = best_neighbor

            if(vc.fitness() < best_fitness):
                best_fitness = vc.fitness()
                best = vc
                if(best_fitness == 0):
                    break
            if(len(tabu_list) > max_tabu_size):
                del tabu_list[0]

        print("Tabu Search")
        print(best_fitness)
        print(best)
        