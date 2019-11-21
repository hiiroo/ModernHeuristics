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

# from CNFFunction import CNFFunction
from tqdm import tqdm
from BooleanGenome import BooleanGenome, CNFFunction
from random import random
from math import exp

class SATSA:

    """
    public void run( int tMax, CNFFunction instance ) {

        BooleanGenome best = null;
        int bestFitness = Integer.MAX_VALUE;
        double temperature = tMax + 1;
        long startTime = System.currentTimeMillis();
        BooleanGenome vc = new BooleanGenome( instance );

        for ( int t = 0; t < tMax; t++ ) {
            for ( int i = 0; i < 10000; i++ ) {
                BooleanGenome vn = vc.getRandomNeighbor();
                if ( vn.getFitness() < vc.getFitness() ) {
                    vc = vn;
                    if ( vc.getFitness() < bestFitness ) {
                        bestFitness = vc.getFitness();
                        best = vc;
                    }
                }
                else {
                    int diff = vc.getFitness() - vn.getFitness();
                    if ( Math.random() < Math.exp( diff / temperature ) ) {
                        vc = vn;
                    }
                }
            }
            temperature--;
        }
        long elapsedTime = System.currentTimeMillis() - startTime;
        System.out.println( "\nSimulated Annealing ran for " + elapsedTime + " milliseconds" );
        System.out.println( "Best Fitness: " + bestFitness );
        System.out.println( best );
    }
    """    
    @staticmethod
    def run(tMax:int, instance:CNFFunction):
        best = None
        best_fitness = 1e10
        temperature = tMax+1
        vc = BooleanGenome(instance)

        for t in tqdm(range(tMax)):
            for i in range(10000):
                vn = vc.random_neighbor()
                if(vn.fitness() < vc.fitness()):
                    vc = vn
                    if(vc.fitness() < best_fitness):
                        best_fitness = vc.fitness()
                        best = vc
                else:
                    diff = vc.fitness() - vn.fitness()
                    if(random() < exp(diff/temperature)):
                        vc = vn
            temperature-=1

        print("Simulated Annealing")
        print(best_fitness)
        print(best)
        