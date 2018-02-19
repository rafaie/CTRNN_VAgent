import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def inverseSigmoid(x):
    return math.log(x/(1-x))
