from math import sin
import numpy as np
import random

''' Icmic混沌初始化 '''


def Icmic_initial(X, pop, ub):

    A = 70

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.152
        else:
            for j in range(len(X[i])):
                if X[i - 1, j] == 0:
                    X[i - 1, j] = 0.152
                X[i, j] = sin(A / X[i - 1, j])


    for i in range(pop):
        X[i, :] = X[i, :] * ub

    return X


def Icmic(C):

    A = 70

    if C == 0:
        C = 0.152
    p = sin(A / C)

    return p
