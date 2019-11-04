


from TSPInstance import TSPInstance
from TSPDescent import TSPDescent
from TSPA import TSPA
from TSPTS import TSPTS


if __name__ == "__main__":
    instance = TSPInstance("berlin52.tsp")

    TSPDescent.run(100, instance)
    TSPA.run(1000, instance)
    TSPTS.run(30000, instance, 400)
