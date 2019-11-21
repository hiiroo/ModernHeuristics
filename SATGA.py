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

from random import random, randint, shuffle
from typing import List
from tqdm import tqdm
from BooleanGenome import BooleanGenome, CNFFunction


class SATGA:

    def __init__(self):
        self.population: List[BooleanGenome] = []

    """
    private double[] constructRouletteWheel( int populationSize ) {
        //parent selection - roulette wheel construction
        double sum = 0;
        for ( int popCount = 0; popCount < populationSize; popCount++ ) {
            sum += 1.0 / population.get( popCount ).getFitness();
        }
        double[] probabilities = new double[populationSize];
        probabilities[ 0 ] = 0;
        for ( int popCount = 0; popCount < populationSize - 1; popCount++ ) {
            probabilities[ popCount + 1 ] = probabilities[ popCount ]
                    + (1.0 / population.get( popCount ).getFitness()) / sum;
        }
        return probabilities;
    }
    """

    def construct_roulette_wheel(self, population_size: int) -> List[float]:
        sum = 0.0

        for pop_count in range(population_size):
            sum += 1/(self.population[pop_count].fitness())

        probabilities: List[float] = []
        probabilities[0] = 0

        for pop_count in range(population_size - 1):
            probabilities[pop_count + 1] = probabilities[pop_count] + \
                (1/self.population[pop_count].fitness)/sum

        return probabilities

    """
    private List<BooleanGenome> rouletteWheelSelection( int populationSize ) {
        double[] probabilities = constructRouletteWheel( populationSize );
        //parent selection
        List<BooleanGenome> matingPool = new ArrayList<>();
        for ( int popCount = 0; popCount < populationSize; popCount++ ) {
            double rand = Math.random();
            int selectedParent = -1;
            for ( int probCount = 1; probCount < populationSize; probCount++ ) {
//                    System.out.println( rand + " " + probabilities[ probCount ]  );
                if ( probabilities[ probCount ] > rand ) {
                    selectedParent = probCount - 1;
                    break;
                }
            }
            if ( selectedParent == - 1 ) {
                selectedParent = populationSize - 1;
            }

            matingPool.add( population.get( selectedParent ) );
        }
        return matingPool;
    }
    """

    def roulette_wheel_selection(self, population_size: int) -> List[BooleanGenome]:
        probabilities = self.construct_roulette_wheel(population_size)
        mating_pool: List[BooleanGenome] = []

        for prob_count in range(population_size):
            if(probabilities[prob_count] > random()):
                selected_parent = prob_count-1
                break

        if(selected_parent == -1):
            selected_parent = population_size - 1

        mating_pool.append(self.population[selected_parent])

        return mating_pool

    """
    private List<BooleanGenome> SUS( int populationSize ) {
        double[] probabilities = constructRouletteWheel( populationSize );
        //parent selection
        List<BooleanGenome> matingPool = new ArrayList<>();
        Random r = new Random();
        double rand = (( double ) (r.nextInt( populationSize )) / populationSize) / populationSize;
    //        System.out.println( rand );
        for ( int popCount = 0; popCount < populationSize; popCount++ ) {
            int selectedParent = -1;
            for ( int probCount = 1; probCount < populationSize; probCount++ ) {
    //                    System.out.println( rand + " " + probabilities[ probCount ]  );
                if ( probabilities[ probCount ] > rand ) {
                    selectedParent = probCount - 1;
                    break;
                }
            }
            if ( selectedParent == - 1 ) {
                selectedParent = populationSize - 1;
            }

            matingPool.add( population.get( selectedParent ) );
            rand += 1.0 / populationSize;
        }
        return matingPool;
    }
    """

    def SUS(self, population_size: int) -> List[BooleanGenome]:
        probabilities = self.construct_roulette_wheel(population_size)

        mating_pool: List[BooleanGenome] = []
        rand = (randint(0, population_size)/population_size)/population_size

        for pop_count in population_size:
            selected_parent = -1
            for prob_count in population_size:
                if(probabilities[prob_count] > rand):
                    selected_parent = prob_count - 1
                    break
            if(selected_parent == -1):
                selected_parent = population_size - 1

            mating_pool.append(self.population[selected_parent])
            rand += 1/population_size

        return mating_pool

    """
    private List<BooleanGenome> tournamentSelection( int tournamentSize, int populationSize ) {
        List<BooleanGenome> matingPool = new ArrayList<>();
        Random r = new Random();
        for ( int i = 0; i < populationSize; i++ ) {
            int bestFitness = Integer.MAX_VALUE;
            BooleanGenome bestCandidate = null;
            for ( int j = 0; j < tournamentSize; j++ ) {
                int index = r.nextInt( tournamentSize );
                BooleanGenome curr = population.get( index );
                if ( curr.getFitness() < bestFitness ) {
                    bestFitness = curr.getFitness();
                    bestCandidate = curr;
                }
            }
            matingPool.add( bestCandidate );
        }
        return matingPool;
    }
    """
    def tournament_selection(self, tournament_size: int, population_size: int) -> List[BooleanGenome]:
        mating_pool: List[BooleanGenome] = []

        for i in range(population_size):
            index = randint(0, tournament_size)
            best_candidate = self.population[index]
            
            for j in range(tournament_size-1):
                index = randint(0, tournament_size)
                curr = self.population[index]
                
                if(curr.fitness() < best_candidate.fitness()):
                    best_candidate = curr

            mating_pool.append(best_candidate)

        return mating_pool

    """
    private void crossover( BooleanGenome parent1, BooleanGenome parent2, List<BooleanGenome> population ) {
        Random r = new Random();
        int crossOverPoint = r.nextInt( parent1.getSize() - 1 );
        BooleanGenome child1 = new BooleanGenome( parent1 );
        for ( int i = crossOverPoint + 1; i < parent1.getSize(); i++ ) {
            child1.setGene( i, parent2.getGene( i ) );
        }
        BooleanGenome child2 = new BooleanGenome( parent2 );
        for ( int i = crossOverPoint + 1; i < parent1.getSize(); i++ ) {
            child2.setGene( i, parent1.getGene( i ) );
        }
        population.add( child1 );
        population.add( child2 );
    }
    """

    def crossover(self, parent1: BooleanGenome, parent2: BooleanGenome, population: List[BooleanGenome]):
        crossover_point = randint(0, len(parent1)-1)
        child1 = BooleanGenome.from_BooleanGenome(parent1)

        for i in range(crossover_point+1, len(parent1)):
            child1.set_gene(i=i, value=parent2.get_gene(i))

        child2 = BooleanGenome.from_BooleanGenome(parent2)

        for i in range(crossover_point+1, len(parent2)):
            child2.set_gene(i=i, value=parent1.get_gene(i))

        population.append(child1)
        population.append(child2)

    def run(self, n_generations: int, population_size: int, crossover_rate: float, mutation_rate: float, instance: CNFFunction):
        self.population: List[BooleanGenome] = []

        for i in range(population_size):
            gene = BooleanGenome(instance)
            self.population.append(gene)

        best:BooleanGenome = self.population[0]
        for pop_gene in self.population:
            if(pop_gene.fitness() < best.fitness()):
                best = BooleanGenome.from_BooleanGenome(pop_gene)

        for i in tqdm(range(n_generations)):
            mating_pool = self.tournament_selection(10, population_size)

            shuffle(mating_pool)
            self.population.clear()
            # crossover
            for pool_count in range(0, len(mating_pool), 2):
                rand = random()
                if(rand < crossover_rate):
                    self.crossover(
                        mating_pool[pool_count], mating_pool[pool_count + 1], self.population)
                else:
                    self.population.append(mating_pool[pool_count])
                    self.population.append(mating_pool[pool_count + 1])
            # mutation
            for pop_count in range(len(mating_pool)):
                for gene_count in range(instance.n_variables):
                    if(random() < mutation_rate):
                        self.population[pop_count].flip_gene(gene_count)

            for pop_count in range(len(self.population)):
                if(self.population[pop_count].fitness() < best.fitness()):
                    best = BooleanGenome.from_BooleanGenome(self.population[pop_count])

            del self.population[randint(0, len(self.population)-1)]
            self.population.append(best)

            if(best.fitness() == 0):
                break

        for pop_count in range(len(self.population)):
            if(self.population[pop_count].fitness() < best_fitness):
                best_fitness = self.population[i].fitness()
                best = self.population[i]

        print("SAT in GA")
        print(best_fitness)
        print(best)
