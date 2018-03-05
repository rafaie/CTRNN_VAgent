"""
ga_function_optimization.py: Using genetic_algorithm for to find the best
parameters for the CTRNN

"""

import logging.config
import yaml
import time
import csv
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

__author__ = "Mostafa Rafaie"
__license__ = "APLv2"

# dataset
dataset_path = 'dataset.csv'
dataset = []


def load_dataset():
    dataset = []

    with open('dataset.csv', 'r') as fi:
        csv_file = csv.reader(fi, delimiter=',',
                              quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for row in csv_file:
            dataset.append(row)


# Using inverse function for fitness 1/F(x)
def calc_fitness(genom):
    pass


if __name__ == "__main__":
    logging.config.dictConfig(yaml.load(
                              open('genetic_algorithm/logging.yaml')))

    path = 'genetic_algorithm/sample_genom_struct.csv'
    init_population_size = 10000
    population_size = 200
    mutation_rate = 0.20
    num_iteratitions = 400
    crossover_type = GeneticAlgorithm.TWO_POINT_CROSSOVER
    fitness_goal = 0.00001

    load_dataset()

    # ga = GeneticAlgorithm(path)
    #
    # start_time = time.time()
    # population = ga.run(init_population_size, population_size,
    #                     mutation_rate, num_iteratitions, crossover_type,
    #                     calc_fitness, fitness_goal,
    #                     cuncurrency=1,
    #                     reverse_fitness_order=False)
    # end_time = time.time()
    # print(population[:3].astype(float))
    # print(population[:, -1].astype(float))
    # print('Runtime :', end_time - start_time)
