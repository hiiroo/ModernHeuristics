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

from math import inf
from tqdm import tqdm
from NLPProblem3D import NLPProblem3D
from RealNumberGenome import RealNumberGenome

class NLPDescent:


    """
    public void run(int tMax, NLPProblem3D instance) {
        
        RealNumberGenome best = null;
        double bestFitness = Double.NEGATIVE_INFINITY;
        
        for ( int t = 0; t < tMax; t++ ) {
            boolean local = false;
            RealNumberGenome vc = new RealNumberGenome(instance);
            while (!local) {
                RealNumberGenome vn = vc.getBestNeighbor(0.1);
                if ( vn!= null && vn.getFitness() > vc.getFitness() ) {
                    vc = vn;        
                }
                else
                    local = true;
            }
            if (vc.getFitness() > bestFitness ) {
                bestFitness=vc.getFitness();
                best = vc;
            }
        }
        System.out.println( bestFitness );
        System.out.println( best );
    }
    """
    @staticmethod
    def run(tMax:int, instance:NLPProblem3D):
        best = None
        best_fitness = -inf

        for t in tqdm(range(tMax)):
            local = False
            vc = RealNumberGenome.from_instance(instance)
            while(not local):
                vn = vc.best_neighbor(1e-1)
                if((vn != None) and (vn.fitness() > vc.fitness())):
                    vc = vn
                else:
                    local = True

            if(vc.fitness() > best_fitness):
                best_fitness = vc.fitness()
                best = vc

        print(best_fitness)
        print(best)
