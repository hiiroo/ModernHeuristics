

from time import time
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
            vc.two_opt()
            while(not local):
                if vc.fitness == 7542 :  break
                vn = vc.best_neighbor()
                vn.two_opt()
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
        
