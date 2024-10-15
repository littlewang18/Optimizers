import numpy as np
import random

''' PWLCM混沌初始化 '''

def Pwlcm_initial(X, pop, ub ):

    P = 0.7

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.002
        elif 0 < X[i - 1 , 0] < P:
            X[i, :] = X[i - 1, :] / P
        else:
            X[i, :] = (1 - P) * (1 - X[i - 1, :])


    for i in range(pop):
        X[i, :] = X[i, :] * ub

    return X


def Pwlcm(A):

    P = 0.7


    if 0 < A < P:
        p = A / P
    else:
        p = (1 - P) * (1 - A)

    return p
