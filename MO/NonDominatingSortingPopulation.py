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
from Genome import Genome
from Population import Population
from NonDominatedPopulation import NonDominatedPopulation
from Comparators import FitnessComparator, compare_rank

class NonDominatingSortingPopulation(Population):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def calculate_crowding_distance(self, archive:NonDominatedPopulation):
        for i in range(len(archive)):
            archive.get_genome(i).crowding_distance(0)

        for i in range(archive.get_genome(0).nobjectives):
            archive.sort(FitnessComparator(i))
            min:float = archive.get_genome(0).fitness[i]
            max:float = archive.get_genome(-1).fitness[i]
            archive.get_genome(0).crowding_distance(2)
            archive.get_genome(-1).crowding_distance(2)

            for j in range(len(archive)):
                distance:float = (archive.get_genome(j+1).fitness[i] - archive.get_genome(j-1).fitness[i] - min) / (max - min)
                archive.get_genome(j).crowding_distance(distance + archive.get_genome(j).crowding_distance)


    def rank(self): 
        for i in range(len(self)):
            super().get_genome(i).rank = -1

        current_rank:int = 1

        while(True):
            archive:NonDominatedPopulation = NonDominatedPopulation()

            for i in range(len(self)):
                current_genome:Genome = super().get_genome(i)
                if(current_genome.rank == -1):
                    archive.add_genome(current_genome)

            if (len(archive) == 0):
                break

            for i in range(len(archive)):
                archive.get_genome(i).rank = current_rank


    def truncate(self, population_size:int):
        super().sort(compare_rank)
        while(len(self) > population_size):
            self.remove_genome(-1)

    def __str__(self):
        return super().__str__()
        