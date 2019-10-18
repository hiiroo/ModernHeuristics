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
from TSPInstance import TSPInstance
from PermutationGenome import PermutationGenome

class TSPDescent:


    """
    public void run(int tMax, TSPInstance instance) {
        
        PermutationGenome best = null;
        int bestFitness = Integer.MAX_VALUE;
        
        for ( int t = 0; t < tMax; t++ ) {
            boolean local = false;
            PermutationGenome vc = new PermutationGenome(52, instance);
            
            while (!local) {
                if ( vc.getFitness() == 7542 ) break;
                PermutationGenome vn = vc.getBestNeighbor();
                if ( vn.getFitness() < vc.getFitness() ) {
                    vc = vn;                  
                }
                else
                    local = true;
            }
            if (vc.getFitness() < bestFitness ) {
                bestFitness=vc.getFitness();
                best = vc;
            }
        }
        System.out.println( bestFitness );
    }
    """
    @staticmethod
    def run(tMax:int, instance:TSPInstance):
        best = None
        best_fitness = 1e10

        for t in tqdm(range(tMax)):
            local = False
            vc = PermutationGenome.from_instance(52, instance)

            while(not local):
                if vc.fitness == 7542 :  break
                vn = vc.best_neighbor()
                if(vn.fitness() < vc.fitness()):
                    vc = vn
                else:
                    local = True

            if vc.fitness() < best_fitness:
                best_fitness = vc.fitness()
                best = vc
        
        print(best_fitness)

if __name__ == "__main__":
    tsp_instance = TSPInstance("berlin52.tsp")
    tsp_instance.read_data()
    TSPDescent.run(50, tsp_instance)
