import random
import numpy
import math
from solution import solution
import time



def SSA(objf, lb, ub, dim, N, Max_iteration):

    if not isinstance(lb, list):
        lb = [lb] * dim
    if not isinstance(ub, list):
        ub = [ub] * dim
    Convergence_curve = numpy.zeros(Max_iteration)

    # Initialize the positions of salps
    SalpPositions = numpy.zeros((N, dim))
    for i in range(dim):
        SalpPositions[:, i] = numpy.random.uniform(
            0, 1, N) * (ub[i] - lb[i]) + lb[i]
    SalpFitness = numpy.full(N, float("inf"))

    FoodPosition = numpy.zeros(dim)
    FoodFitness = float("inf")
    # Moth_fitness=numpy.fell(float("inf"))

    s = solution()

    print('SSA is optimizing  "' + objf.__name__ + '"')

    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")

    for i in range(0, N):
        # evaluate moths
        SalpFitness[i] = objf(SalpPositions[i, :])

    sorted_salps_fitness = numpy.sort(SalpFitness)
    I = numpy.argsort(SalpFitness)

    Sorted_salps = numpy.copy(SalpPositions[I, :])

    FoodPosition = numpy.copy(Sorted_salps[0, :])
    FoodFitness = sorted_salps_fitness[0]

    Iteration = 1

    # Main loop
    while Iteration < Max_iteration:

        # Number of flames Eq. (3.14) in the paper
        # Flame_no=round(N-Iteration*((N-1)/Max_iteration));

        c1 = 2 * math.exp(-((4 * Iteration / Max_iteration) ** 2))
        # Eq. (3.2) in the paper

        for i in range(0, N):

            SalpPositions = numpy.transpose(SalpPositions)

            if i < N / 2:
                for j in range(0, dim):
                    c2 = random.random()
                    c3 = random.random()
                    # Eq. (3.1) in the paper
                    if c3 < 0.5:
                        SalpPositions[j, i] = FoodPosition[j] + c1 * (
                            (ub[j] - lb[j]) * c2 + lb[j]
                        )
                    else:
                        SalpPositions[j, i] = FoodPosition[j] - c1 * (
                            (ub[j] - lb[j]) * c2 + lb[j]
                        )

                    ####################

            elif i >= N / 2 and i < N + 1:
                point1 = SalpPositions[:, i - 1]
                point2 = SalpPositions[:, i]

                SalpPositions[:, i] = (point2 + point1) / 2
                # Eq. (3.4) in the paper

            SalpPositions = numpy.transpose(SalpPositions)

        for i in range(0, N):

            # Check if salps go out of the search spaceand bring it back
            for j in range(dim):
                SalpPositions[i, j] = numpy.clip(
                    SalpPositions[i, j], lb[j], ub[j])

            SalpFitness[i] = objf(SalpPositions[i, :])

            if SalpFitness[i] < FoodFitness:
                FoodPosition = numpy.copy(SalpPositions[i, :])
                FoodFitness = SalpFitness[i]

        # Display best fitness along the iteration

        Convergence_curve[Iteration] = FoodFitness

        Iteration = Iteration + 1

    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.optimizer = "SSA"
    s.testfun = objf.__name__
    s.best = FoodFitness
    s.bestX = FoodPosition
    s.convergence = Convergence_curve
    return s


# ''' 初始化函数 '''
# def initial(pop, dim, ub, fun):
#     X = np.zeros((pop, dim))
#     fit = np.zeros((pop, 1))

#     for i in range (pop):
#         X[i, :] = ub * np.random.rand(1, dim)

#     for i in range(pop):
#         fit[i, 0] = fun(X[i, :])

#     return X, fit


# '''边界检测'''


# def BorderCheck(s, lb, ub):
#     temp = s
#     for i in range(len(s)):
#         if temp[i] < lb[0, i]:
#             temp[i] = lb[0, i]
#         elif temp[i] > ub[0, i]:
#             temp[i] = ub[0, i]

#     return temp


# '''SSA'''


# def SSA(fun, lb, ub, dim, pop, MaxIter):

#     ub = ub * np.ones((1, dim))
#     lb = lb * np.ones((1, dim))

#     # 生产者的人口规模占总人口规模的20%
#     pNum = round(pop * 0.2)
#     X, fit = initial(pop, dim, ub, fun)                    # 初始化种群与适应度函数

#     Curve = np.zeros([MaxIter])                                # 初始化收敛曲线

#     pFit = fit                                                 # 最佳适应度矩阵
#     pX = X                                                     # 最佳种群位置

#     fMin = np.min(fit[:, 0])                                   # 最优适应度
#     bestX = X[np.argmin(fit[:, 0]), :]                         # 最优位置

#     s = solution()
#     timerStart = time.time()
#     s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")


#     for t in range(MaxIter):                                   # 迭代更新


#         sortIndex = np.argsort(pFit.T)                         # 适应度排序
#         fmax = np.max(pFit[:, 0])                              # 最差适应度
#         worse = X[np.argmax(pFit[:, 0]), :]                    # 最差位置

#         #发现者（探索者）的位置更新
#         # 预警值
#         r2 = np.random.rand(1)
#         if r2 < 0.8:                                                                        # 预警值小，没有捕食者
#             for i in range(pNum):
#                 r1 = np.random.rand(1)
#                 X[sortIndex[0, i], :] = pX[sortIndex[0, i], :] * \
#                     np.exp(-(i) / (r1 * MaxIter))
#                 X[sortIndex[0, i], :] = BorderCheck(
#                     X[sortIndex[0, i], :], lb, ub)
#                 fit[sortIndex[0, i], 0] = fun(X[sortIndex[0, i], :])
#         elif r2 >= 0.8:                                                                     # 预警值大，更改地方 plus 莱维飞行
#             for i in range(pNum):
#                 Q = np.random.rand(1)
#                 X[sortIndex[0, i], :] = pX[sortIndex[0, i], :] + \
#                     Q * np.ones((1, dim))
#                 X[sortIndex[0, i], :] = BorderCheck(
#                     X[sortIndex[0, i], :], lb, ub)
#                 fit[sortIndex[0, i], 0] = fun(X[sortIndex[0, i], :])

#         bestXX = X[np.argmin(fit[:, 0]), :]


#         # 加入者（追随者）的位置更新
#         for ii in range(pop - pNum):
#             i = ii + pNum
#             A = np.floor(np.random.rand(1, dim) * 2) * 2 - 1
#             if i > pop / 2:  # 这个代表这部分麻雀处于十分饥饿的状态（因为它们的能量很低，也就是适应度值很差），需要到其它地方觅食
#                 Q = np.random.rand(1)
#                 X[sortIndex[0, i], :] = Q * \
#                     np.exp(worse-pX[sortIndex[0, i], :] / np.square(i))
#             # 这一部分追随者是围绕最好的发现者周围进行觅食，其间也有可能发生食物的争夺，使其自己变成生产者
#             else:
#                 X[sortIndex[0,i],:] = bestXX + np.dot(np.abs(pX[sortIndex[0,i],:] - bestXX),
#                                 1 / (A.T*np.dot(A, A.T))) * np.ones((1, dim))
#             X[sortIndex[0, i], :] = BorderCheck(X[sortIndex[0, i], :], lb, ub)
#             fit[sortIndex[0, i], 0] = fun(X[sortIndex[0, i], :])


#         #意识到危险的位置更新
#         arrc = np.arange(len(sortIndex[0, :]))
#         c = np.random.permutation(arrc)
#         b = sortIndex[0, c[0:10]]

#         for j in range(len(b)):

#             if pFit[sortIndex[0, b[j]], 0] > fMin:
#                 X[sortIndex[0,b[j]],:] = bestX+np.random.rand(1,dim) * np.abs(pX[sortIndex[0,b[j]],:] - bestX)
#             else:
#                 X[sortIndex[0, b[j]], :] = pX[sortIndex[0, b[j]], :] + (2 * np.random.rand(1) - 1) * np.abs(
#                     pX[sortIndex[0, b[j]], :] - worse) / (pFit[sortIndex[0, b[j]]]-fmax+10**(-50))

#             X[sortIndex[0, b[j]], :] = BorderCheck(
#                 X[sortIndex[0, b[j]], :], lb, ub)
#             fit[sortIndex[0, b[j]], 0] = fun(X[sortIndex[0, b[j]]])

#         for i in range(pop):
#             if fit[i, 0] < pFit[i, 0]:
#                 pFit[i, 0] = fit[i, 0]
#                 pX[i, :] = X[i, :]
#             if pFit[i, 0] < fMin:
#                 fMin = pFit[i, 0]
#                 bestX = pX[i, :]

#         Curve[t] = fMin

#     timerEnd = time.time()
#     s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
#     s.executionTime = timerEnd - timerStart
#     s.optimizer = "SSA"
#     s.testfun = fun.__name__
#     s.best = fMin
#     s.bestX = bestX
#     s.convergence = Curve

#     return s
