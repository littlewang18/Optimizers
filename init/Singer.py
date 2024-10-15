import numpy as np
import random

''' Singer混沌初始化 '''


def Singer_initial(X, pop, ub):

    U = 1.073

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.152
        else:
            X[i, :] = U * (7.86 * X[i-1, :] - 23.31 * pow((X[i-1, :]), 2) + 28.75 * pow((X[i-1, :]), 3) - 13.302875 * pow((X[i-1, :]), 4))
            
    for i in range(pop):
        X[i, :] = X[i, :] * ub


    return X


def Singer(A):

    U = 1.073


    p = U * (7.86 * A - 23.31 *pow((A), 2) - 13.302875 * pow((A), 4))

    return p

# X = np.zeros((3, 3))

# print(Singer_initial(X, 3, 3, -100, 100))
