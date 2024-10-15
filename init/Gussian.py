import numpy as np


''' Gussian混沌初始化 '''


def Gussian_initial(X, pop, ub):

    U = 1

    for i in range(pop):
        if i == 0 :
            X[i, :] = 0.152
        else:
            if X[i - 1, 0] == 0:
                X[i - 1, :] == 0.152
            X[i, :] = U / (X[i - 1, :] % 1)

    for i in range(pop):
        X[i, :] = X[i, :] * ub


    return X


def Gussian(A):

    U = 1

    p = U / A % 1

    return p
