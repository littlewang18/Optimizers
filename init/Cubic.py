''' Cubic混沌初始化 '''


def Cubic_initial(X, pop, ub):

    P = 2.59

    for i in range(pop):
        if i == 0:
            X[i, :] = 0.242
        else:
            X[i, :] = P * X[i - 1, :] * (1 - pow(X[i - 1, :], 2))

    for i in range(pop):
        X[i, :] = X[i, :] * ub


    return X


def Cubic(A):
    P = 2.59

    p = P * A * (1 - pow(A, 2))

    return p
