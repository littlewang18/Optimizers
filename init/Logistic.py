import numpy as np

''' Logistic混沌初始化 '''

def Logistic_initial(X, pop, ub):

    U = 4

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.152
        else:
            X[i, :] = U * X[i - 1, :] * (1 - X[i - 1, :])

    for i in range(pop):
        X[i, :] = X[i, :] * ub
    return X


def Logistic(A):

    U = 4

    p = U * A * (1 - A)

    return p
