"""
MIT License

Copyright (c) 2019 Ali Mert Ceylan, Adopted from original resources provided 
by Korhan Karabulut for COMP 5658 Modern Heuristics Graduate Course

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

from BooleanGenome import BooleanGenome, FitnessMode
from ZOKSInstance import ZOKSInstance
from ZOKSGA import ZOKSGA, TournamentType

if __name__ == "__main__":
    instance = ZOKSInstance("knapPI_1_100_1000_1")
    zoksga = ZOKSGA()

    # print("Penalty Mode")
    # BooleanGenome.fitness_mode = FitnessMode.Penalty
    # BooleanGenome.penalty_value = 80
    # zoksga.run(5000, 100, 0.8, 0.01, instance, TournamentType.FITNESS)
    
    # print("\nDeath Penalty Mode")
    # BooleanGenome.fitness_mode = FitnessMode.DeathPenalty
    # zoksga.run(5000, 100, 0.8, 0.01, instance, TournamentType.FITNESS)

    # print("\nSuperior Feasibility Mode")
    # BooleanGenome.fitness_mode = FitnessMode.Regular
    # zoksga.run(5000, 100, 0.8, 0.01, instance, TournamentType.SoF)

    print("\nRepair Mode")
    BooleanGenome.fitness_mode = FitnessMode.Repair
    zoksga.run(5000, 100, 0.8, 0.01, instance, TournamentType.FITNESS)
