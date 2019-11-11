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
from BooleanGenome import BooleanGenome, BooleanFunction
from CNFFunction import CNFFunction

"""
public void run( int tMax, CNFFunction instance ) {

    BooleanGenome best = null;
    int bestFitness = Integer.MAX_VALUE;
    long startTime = System.currentTimeMillis();

    for ( int t = 0; t < tMax; t++ ) {
        boolean local = false;
        BooleanGenome vc = new BooleanGenome( instance );
        while ( !local ) {
            BooleanGenome vn = vc.getBestNeighbor();
            if ( vn.getFitness() < vc.getFitness() ) {
                vc = vn;
                if ( vc.getFitness() < bestFitness ) {
                    best = vc;
                    bestFitness = vc.getFitness();
                }
            }
            else {
                local = true;
            }
        }
    }
    long elapsedTime = System.currentTimeMillis() - startTime;
    System.out.println( "\nHill Climbing ran for " + elapsedTime + " milliseconds" );
    System.out.println( "Best Fitness: " + bestFitness );
    System.out.println( best );

}
"""
class SATDescent:
    @staticmethod
    def run(tMax:int, instance:CNFFunction):
        bbest = None
        best_fitness = 1e10

        for i in tqdm(range(tMax)):
            blocal = False
            vc = BooleanGenome(instance)
            while(not blocal):
                vn = vc.best_neighbor()
                
                if(vn is not None):
                    bbest = vn
                    break
                if(vn.fitness() < vc.fitness()):
                    vc = vn
                    if(vc.fitness() < best_fitness):
                        bbest = vc
                        best_fitness = vc.fitness()
                else:
                    blocal = True
        
        print("Hill Climbing")
        print(bbest)

