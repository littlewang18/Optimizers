from cmath import pi
from math import sin
import numpy as np

''' Sine混沌初始化 '''


def Sine_initial(X, pop, ub):

    A = 2

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.152
        else:
            for j in range(len(X[i])):
                X[i, j] = 4 / A * sin(pi * X[i - 1, j])

    for i in range(pop):
        X[i, :] = X[i, :] * ub

    return X


def Sine(C):

    A = 2


    p = 4 / A * sin(pi * C)


    return p
