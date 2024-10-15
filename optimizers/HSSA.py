import math
import time
import numpy as np


from solution import solution
from init import Circle
from functools import wraps

  


'''种群初始化'''
def initial(pop, dim, ub, fun):
    X = np.zeros((pop, dim))
    fit = np.zeros((pop, 1))

    X = Circle.Circle_initial( X, pop, ub)

    for i in range(pop):
        fit[i, 0] = fun(X[i, :])



    return X, fit




'''边界检测'''
def BorderCheck(s,lb,ub):
    temp = s
    for i in range(len(s)):
        if temp[i] < lb[0,i]:
            temp[i] = lb[0,i]
        elif temp[i] > ub[0,i]:
            temp[i] = ub[0,i]

    return temp



'''HSSA'''
def HSSA(fun, lb, ub, dim, pop, MaxIter):


    ub = ub * np.ones((1, dim))
    lb = lb * np.ones((1, dim))

    pNum = round(pop * 0.2)                                    # 生产者的人口规模占总人口规模的20%
    X, fit = initial(pop, dim, ub, fun)                        # 初始化种群与适应度函数


    Curve = np.zeros([MaxIter])                                # 初始化收敛曲线


    pFit = fit                                                 # 最佳适应度矩阵
    pX = X                                                     # 最佳种群位置

    fMin = np.min(fit[:,0])                                    # 最优适应度
    bestX = X[np.argmin(fit[:, 0]), :]                         # 最优位置


    g1 = -math.pi                                              # 黄金正弦参数
    g2 = math.pi
    tau = (5 ** 0.5 - 1) / 2
    x1 = g1 * tau + g2 * (1 - tau)
    x2 = g1 * (1 - tau) + g2 * tau

    s = solution()
    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")



    for t in range(MaxIter):                                   # 迭代更新

        sortIndex = np.argsort(pFit.T)                         # 适应度排序
        fmax = np.max(pFit[:,0])                               # 最差适应度
        worse = X[np.argmax(pFit[:, 0]), :]                    # 最差位置



        #发现者（探索者）的位置更新
        r2 = np.random.rand(1)                                                              # 预警值
        if r2 < 0.8:                                                                        # 预警值小，没有捕食者
            for i in range(pNum):
                r1 = np.random.rand(1)
                X[sortIndex[0,i],:] = pX[sortIndex[0,i],:] * np.exp(-(i) / (r1 * MaxIter))
                X[sortIndex[0,i],:] = BorderCheck(X[sortIndex[0,i],:],lb,ub)
                fit[sortIndex[0,i],0] = fun(X[sortIndex[0,i],:])
        elif r2 >= 0.8:                                                                     # 预警值大，更改地方 plus 莱维飞行
            for i in range(pNum):
                Q = np.random.rand(1)
                X[sortIndex[0,i],:] = pX[sortIndex[0,i],:] + Q * np.ones((1,dim))
                X[sortIndex[0,i],:] = BorderCheck(X[sortIndex[0,i],:],lb,ub)
                fit[sortIndex[0,i],0] = fun(X[sortIndex[0,i],:])


        bestXX = X[np.argmin(fit[:, 0]), :]



        # 加入者（追随者）的位置更新
        for ii in range(pop - pNum):
            i = ii + pNum
            A = np.floor(np.random.rand(1,dim) * 2) * 2 - 1
            if i > pop / 2:                                                               #  这个代表这部分麻雀处于十分饥饿的状态（因为它们的能量很低，也就是适应度值很差），需要到其它地方觅食
                Q = np.random.rand(1)
                X[sortIndex[0, i], :] = Q * np.exp(worse-pX[sortIndex[0, i], :] / np.square(i))
            else:                                                                       # 这一部分追随者是围绕最好的发现者周围进行觅食，其间也有可能发生食物的争夺，使其自己变成生产者
                β = 1.5
                σ = ((math.gamma(1 + β)* math.sin(math.pi * β / 2)) / (β * math.gamma((1 + β) / 2)* 2 ** ((β - 1) / 2))) ** 1 / β
                X[sortIndex[0, i], :] = bestXX  + bestXX  *(σ * np.random.randn() / (np.random.randn() ** 1 / β))
            X[sortIndex[0,i],:] = BorderCheck(X[sortIndex[0,i],:], lb, ub)
            fit[sortIndex[0,i],0] = fun(X[sortIndex[0,i], :])




        #意识到危险的位置更新
        arrc = np.arange(len(sortIndex[0,:]))
        c = np.random.permutation(arrc)
        b = sortIndex[0,c[0:10]]


        for j in range(len(b)):
            r3 = np.random.random() * 2 * math.pi
            r4 = np.random.random() * 2 * math.pi
            if X[sortIndex[0, b[j]], :].all() < bestXX.all():
                g2 = x2
                x2 = x1
                x1 = g1 * tau + g2 * (1 - tau)
            else:
                g1 = x1
                x1 = x2
                x2 = g1 * (1 - tau) + g2 * tau
            if x1 == x2:
                g1 = np.random.random()
                g2 = np.random.random()
                x1 = g1 * tau + g2 * (1 - tau)
                x2 = g1 * (1 - tau) + g2 * tau

            if pFit[sortIndex[0,b[j]],0] > fMin:
                X[sortIndex[0, b[j]], :] = X[sortIndex[0, b[j]], :] * abs(np.sin(r3)) + r4 * np.sin(r3) * abs(x1 * bestXX - x2 * X[sortIndex[0, b[j]], :])
            else:
                X[sortIndex[0,b[j]],:] = pX[sortIndex[0,b[j]],:] + (2 * np.random.rand(1) - 1) * np.abs(pX[sortIndex[0,b[j]],:] - worse) / (pFit[sortIndex[0,b[j]]]-fmax+10**(-50))

            X[sortIndex[0,b[j]],:] = BorderCheck(X[sortIndex[0,b[j]],:],lb,ub)
            fit[sortIndex[0,b[j]],0] = fun(X[sortIndex[0,b[j]]])



        for i in range(pop):
            if fit[i,0] < pFit[i,0]:
                pFit[i,0] = fit[i,0]
                pX[i,:] = X[i,:]
            if pFit[i,0] < fMin:
                fMin = pFit[i,0]
                bestX = pX[i,:]

        Curve[t] = fMin

    timerEnd = time.time()
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.optimizer = "HSSA"
    s.testfun = fun.__name__
    s.best = fMin
    s.bestX = bestX
    s.convergence = Curve


    return s


