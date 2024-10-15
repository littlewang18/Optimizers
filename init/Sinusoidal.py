from cmath import pi
from math import sin
import numpy as np


''' Sinusoidal混沌初始化 '''


def Sinusoidal_initial(X, pop, ub):

    A = 2.3

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.74
        else:
            for j in range(len(X[i])):
                X[i, j] = A * pow(X[i - 1, j], 2) * sin(pi * X[i - 1, j])



    for i in range(pop):
        X[i, :] = X[i, :] * ub

    return X


def Sinusoidal(C):

    A = 2.3


    p = A * pow(C, 2) * sin(pi * C)


    return p
