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

from sys import maxsize
from time import time
from tqdm import tqdm
from TSPInstance import TSPInstance
from PermutationGenome import PermutationGenome

class TSPTS:


    """
    public void run( int tMax, TSPInstance instance, int maxTabuSize ) {
        long startTime=System.currentTimeMillis();
        PermutationGenome vc = new PermutationGenome( 52, instance );
        vc.twoOpt();
        List<Integer> tabuList = new ArrayList<>();
        tabuList.add( vc.getFitness() );
        PermutationGenome best = vc;
        int bestFitness = vc.getFitness();

        for ( int t = 0; t < tMax; t++ ) {
            int bestNeighborFitness = Integer.MAX_VALUE;
            PermutationGenome bestNeighbor = null;
            for ( int n = 0; n < 50; n++ ) {
                PermutationGenome temp;
                while ( true ) {
                    temp = vc.getRandomNeighbor();
                    if ( !tabuList.contains( temp.getFitness() ) ) {
                        break;
                    }
                }

                if ( temp.getFitness() < bestNeighborFitness ) {
                    bestNeighbor = temp;
                    bestNeighborFitness = temp.getFitness();
                }

            }
            vc = bestNeighbor;
//            vc = vc.getBestNeighbor( tabuList );
            vc.twoOpt();
            tabuList.add( vc.getFitness() );
            if ( vc.getFitness() < bestFitness ) {
                bestFitness = vc.getFitness();
                best = vc;
            }
            if ( vc.getFitness() == 7542 ) {
                break;
            }
            if ( tabuList.size() > maxTabuSize ) {
                tabuList.remove( 0 );
            }
        }
        long elapsedTime = System.currentTimeMillis() - startTime;
        System.out.println( "Tabu Search ran for " + elapsedTime + " milliseconds" );
        System.out.println( bestFitness );
        System.out.println( best );
    }
    """
    @staticmethod
    def run(tMax:int, instance:TSPInstance, max_tabu_size:int):
        
        vc = PermutationGenome.from_instance(52, instance)
        vc.two_opt()
        tabu_list = []
        tabu_list.append(vc.fitness())
        best = vc
        best_fitness = vc.fitness()
        
        for t in tqdm(range(tMax)):
            best_neighbor_fitness = 1e10
            best_neighbor = None

            for i in range(50):
                temp = None

                while(True):
                    temp = vc.random_neighbor()
                    if(temp.fitness not in tabu_list):
                        break

                if(temp.fitness() < best_neighbor_fitness):
                    best_neighbor = temp
                    best_neighbor_fitness = temp.fitness()
        
            vc = best_neighbor
            # vc = vc.best_neighbor()
            vc.two_opt()
            tabu_list.append(vc.fitness())
            if(vc.fitness() < best_fitness):
                best_fitness = vc.fitness()
                best = vc

            if(vc.fitness() == 7542):
                break

            if(len(tabu_list) > max_tabu_size):
                del tabu_list[0]

        print(best_fitness)

if __name__ == "__main__":
    tsp_instance = TSPInstance("berlin52.tsp")
    tsp_instance.read_data()
    TSPTS.run(50, tsp_instance, 400)
        
