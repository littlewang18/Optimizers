import numpy as np

''' Tent混沌初始化 '''


def Tent_initial(X, pop, ub):

    B = 0.4

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.152
        elif 0 < X[i - 1, 0] <= B:
            X[i, :] = X[i - 1, :] / B
        else:
            X[i, :] = (1 - X[i-1, :]) / (1 - B)

    for i in range(pop):
        X[i, :] = X[i, :] * ub

    return X


def Tent(A):

    B = 0.4

    if 0 < A <= B:
        p = A / B
    else:
        p = (1 - A) / (1 - B)

    return p
