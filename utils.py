import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def inverse_sigmoid(x):
    return math.log(x/(1-x))
