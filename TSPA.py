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

from math import exp
from random import random
from tqdm import tqdm
from TSPInstance import TSPInstance
from PermutationGenome import PermutationGenome

class TSPA:


    """
    public void run(int tMax, TSPInstance instance ) {

        PermutationGenome best = null;
        int bestFitness = Integer.MAX_VALUE;
        int temperature = tMax + 1;
        long startTime=System.currentTimeMillis();
        PermutationGenome vc = new PermutationGenome( 52, instance );

        for ( int t = 0; t < tMax; t++ ) {
            vc.twoOpt();
            for ( int i = 0; i < 1000; i++ ) {

                if ( vc.getFitness() == 7542 ) {
                    break;
                }
                PermutationGenome vn = vc.getRandomNeighbor();
                vn.twoOpt();
                if ( vn.getFitness() < vc.getFitness() ) {
                    vc = vn;
                }
                else {
                    int diff = vc.getFitness() - vn.getFitness();
                    if ( Math.random() < Math.exp( diff / temperature ) ) {
                        vc = vn;
                    }
                }
                if ( vc.getFitness() < bestFitness ) {
                    bestFitness = vc.getFitness();
                    best = vc;
                }
            }
            temperature--;
        }
        long elapsedTime = System.currentTimeMillis() - startTime;
        System.out.println( "Simulated Annealing ran for " + elapsedTime + " milliseconds" );
        System.out.println( bestFitness );
        System.out.println( best );
    }
    """
    @staticmethod
    def run(tMax:int, instance:TSPInstance):
        best = None
        best_fitness = 1e10
        temperature = tMax + 1
        vc = PermutationGenome.from_instance(52, instance)

        for t in tqdm(range(tMax)):
            vc.two_opt()
            
            for i in range(1000):
                if vc.fitness == 7542 :  break
                vn = vc.random_neighbor() #best_neighbor()
                vn.two_opt()
                if(vn.fitness() < vc.fitness()):
                    vc = vn
                else:
                    diff = vc.fitness() - vn.fitness()
                    if(random() < exp(diff/temperature)):
                        vc = vn

                if(vc.fitness() < best_fitness):
                    best_fitness = vc.fitness()
                    best = vc
            
            temperature-=1;
    
        print(best_fitness)
        print(best)

if __name__ == "__main__":
    tsp_instance = TSPInstance("berlin52.tsp")
    tsp_instance.read_data()
    TSPA.run(50, tsp_instance)
