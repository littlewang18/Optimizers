from math import cos
import numpy as np
import matplotlib.pyplot as plt

''' Chebyshev混沌初始化 '''


def Chebyshev_initial(X, pop, ub):

    Q = 5

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.152
        else:
            for j in range(len(X[i])):
                X[i, j] = cos(Q * pow(cos(X[i - 1, j]), -1))


    for i in range(pop):
        X[i, :] = X[i, :] * ub

    return X


def Chebyshev(A):

    Q = 5
    p = cos(Q * pow(cos(A), -1))

    return p


# pop = 10
# dim = 2
# X = np.zeros((pop, dim))
# Q = 5


# for i in range(pop):
#     if i == 0:
#         X[i, 0] = 0.152
#         X[i, 1] = 0.152
#     else:
#         X[i, 0] = cos(Q * pow(cos(X[i - 1, 0]), -1))
#         X[i, 1] = cos(Q * pow(cos(X[i - 1, 1]), -1))


# plt.figure(1)
# for i in range(pop):
#     plt.plot(X[i, 0], 0,  'b.')
#     plt.plot(0, X[i, 1], 'b.')
# plt.show()
