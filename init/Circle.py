from math import pi, sin
import numpy as np
import random

''' Circle 混沌初始化 '''


def Circle_initial(X, pop, ub):

    a = 0.5
    b = 2.2

    for i in range(pop):
        if i == 0:
            for j in range(len(X[i])):
                X[i, j] = random.random()
        else:
            for j in range(len(X[i])):
                X[i, j] = X[i - 1, j] + a - ((b / 2 * pi) * sin(2 * pi * X[i - 1, j])) % 1


    for i in range(pop):
        X[i, :] = X[i, :] * ub
    return X


def Circle(A):

    a = 0.5
    b = 2.2

    p = A + a - ((b / 2 * pi) * sin(2 * pi * A)) % 1

    return p
