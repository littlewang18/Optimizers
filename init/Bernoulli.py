import numpy as np
import random
import matplotlib.pyplot as plt

''' Bernoulli混沌初始化 '''


def Bernoulli_initial(X, pop, ub):

    L = 0.5

    for i in range(pop):
        if i == 0:
            X[i, :] = random.random()
        elif 0 < X[i - 1, 0] <= (1 - L):
            X[i, :] = X[i - 1, :] / (1 - L)
        else:
            X[i, :] = (X[i - 1, :] - 1 + L) / L

    for i in range(pop):
        X[i, :] = X[i, :] * ub

    return X


def Bernoulli(A):

    L = 0.5

    if 0 < A <= (1 - L):
        p = A / (1 - L)
    else:
        p = (A - 1 + L) / L

    return p


# lst = []
# lst.append(random.random())
# c =2000
# for i in range (2000):
#     lst.append(4 * lst[i-1]*(1 - lst[i-1]))


# plt.figure(1)
# plt.plot(lst, '.')
# plt.xlabel('维度')
# plt.ylabel('混沌值')
# plt.figure(2)
# plt.hist(lst)
# plt.xlabel('混沌值')
# plt.ylabel('频数')
# plt.show()