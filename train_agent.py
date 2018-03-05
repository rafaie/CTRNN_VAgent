"""
ga_function_optimization.py: Using genetic_algorithm for to find the best
parameters for the CTRNN

"""

import logging.config
import yaml
import numpy as np
import os
import sys
import random
import time
import csv
import math
from visual_object import Line, Circle
from visual_agent import VisualAgent
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

__author__ = "Mostafa Rafaie"
__license__ = "APLv2"

# CONSTANT
LINE = 1
CIRCLE = 2
STEP_SIZE = 0.1


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


def create_agent(genom):
    agent = VisualAgent()

    path = "categorize.ns"
    if os.path.exists(path) is False:
        print('The network file is Not exit')
        sys.exit(1)

    agent.nervous_system.load(path)

    return agent


def run_process(data, agent, show_details=False):
    obj_id = data[0]
    x1 = data[1]
    y1 = data[2]
    x2 = data[3]
    y2 = data[4]
    goal_x = data[5]
    goal_y = data[6]

    if obj_id == LINE:
        obj = Line()
    else:
        obj = Circle()

    # Run the agent
    random.seed()
    agent.reset(0, y1)
    agent.set_positionX(x1)
    obj.set_positionX(x2)
    obj.set_positionY(y2)

    timer = 0
    status = 0
    start_time = time.time()

    t = 0
    if show_details is True:
        agent.nervous_system.print_model_abstract()

    while obj.positionY() > VisualAgent.BODY_SIZE/2:
        t += STEP_SIZE
        timer += 1
        if show_details is True:
            print("------------------")
            print(agent.positionX(), agent.positionY())
            print(obj.positionX(), obj.positionY())

        status = 1
        agent.step(STEP_SIZE, obj, show_details=show_details)
        obj.step(STEP_SIZE)
        if show_details is True:
            agent.nervous_system.print_model_abstract()

    status += 1
    end_time = time.time()
    if show_details is True:
        print('finished computation at', end_time, ', elapsed time: ',
              end_time - start_time)

    return math.sqrt((agent.positionX() - goal_x) ** 2 +
                     (agent.positionY() - goal_y) ** 2)


# Using inverse function for fitness 1/F(x)
def calc_fitness(genom):
    fitness = []
    agent = create_agent(genom)

    for data in dataset:
        fitness.append(run_process(data, agent))

    return np.median(fitness)


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

    ga = GeneticAlgorithm(path)

    start_time = time.time()
    population = ga.run(init_population_size, population_size,
                        mutation_rate, num_iteratitions, crossover_type,
                        calc_fitness, fitness_goal,
                        cuncurrency=1,
                        reverse_fitness_order=False)
    end_time = time.time()
    print(population[:3].astype(float))
    print(population[:, -1].astype(float))
    print('Runtime :', end_time - start_time)
