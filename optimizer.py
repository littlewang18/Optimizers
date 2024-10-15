import csv
import numpy
import time
import warnings
import plot_convergence as conv_plot
import plot_boxplot as box_plot
from asyncio.windows_events import NULL
from pathlib import Path


import optimizers.GWO as gwo
import optimizers.WOA as woa
import optimizers.SSA as ssa
import optimizers.HSSA as hssa
import optimizers.PSO as pso
import optimizers.MVO as mvo
import optimizers.MFO as mfo
import optimizers.CS as cs
import optimizers.BAT as bat
import optimizers.FFA as ffa
import optimizers.GA as ga
import optimizers.HHO as hho
import optimizers.SCA as sca
import optimizers.JAYA as jaya
import optimizers.DE as de
import TestFun



warnings.simplefilter(action="ignore")


def selector(algo, func_details, pop, MaxIter):
    function_name = func_details[0]
    lb = func_details[1]
    ub = func_details[2]
    dim = func_details[3]

    if algo == "SSA":
        x = ssa.SSA(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "HSSA":
        x = hssa.HSSA(getattr(TestFun, function_name),lb, ub, dim, pop, MaxIter)
    elif algo == "BAT":
        x = bat.BAT(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "PSO":
        x = pso.PSO(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "GA":
        x = ga.GA(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "BAT":
        x = bat.BAT(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "FFA":
        x = ffa.FFA(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "GWO":
        x = gwo.GWO(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "WOA":
        x = woa.WOA(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "MVO":
        x = mvo.MVO(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "MFO":
        x = mfo.MFO(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "CS":
        x = cs.CS(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "HHO":
        x = hho.HHO(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "SCA":
        x = sca.SCA(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "JAYA":
        x = jaya.JAYA(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    elif algo == "DE":
        x = de.DE(getattr(TestFun, function_name), lb, ub, dim, pop, MaxIter)
    else:
        return NULL
    return x


def run(optimizer, objectivefunc, NumOfRuns, params, export_flags):

    # 参数初始化
    PopulationSize = params["PopulationSize"]
    Iterations = params["Iterations"]


    # 保存数据
    Export = export_flags["Export_avg"]
    Export_details = export_flags["Export_details"]
    Export_convergence = export_flags["Export_convergence"]
    Export_boxplot = export_flags["Export_boxplot"]

    Flag = False
    Flag_details = False

    CnvgHeader = []

    results_directory = time.strftime("%Y-%m-%d-%H-%M-%S") + "/"
    Path(results_directory).mkdir(parents=True, exist_ok=True)

    for l in range(0, Iterations):
        CnvgHeader.append("Iter" + str(l + 1))


    for i in range(0, len(optimizer)):
        for j in range(0, len(objectivefunc)):

            convergence = [0] * NumOfRuns
            executionTime = [0] * NumOfRuns

            for k in range(0, NumOfRuns):
                func_details = TestFun.getFunctionDetails(objectivefunc[j])
                x = selector(optimizer[i], func_details, PopulationSize, Iterations)

                # print(x.bestX)
                convergence[k] = x.convergence
                optimizerName = x.optimizer
                testfun = x.testfun

                # 数据写入文件
                if Export_details == True:
                    ExportToFile = results_directory + "experiment_details.csv"
                    with open(ExportToFile, "a", newline="\n") as out:
                        writer = csv.writer(out, delimiter=",")
                        if (Flag_details == False):
                            header = numpy.concatenate([["Optimizer", "Testfun", "ExecutionTime"], CnvgHeader])
                            writer.writerow(header)
                            Flag_details = True
                        a = numpy.concatenate([[x.optimizer, x.testfun, x.executionTime], x.convergence])
                        writer.writerow(a)
                    out.close()


             # 数据写入文件
            if Export == True:
                ExportToFile = results_directory + "experiment.csv"
                with open(ExportToFile, "a", newline="\n") as out:
                    writer = csv.writer(out, delimiter=",")
                    if ( Flag == False):
                        header = numpy.concatenate( [["Optimizer", "Testfun", "ExecutionTime"], CnvgHeader] )
                        writer.writerow(header)
                        Flag = True
                    avgExecutionTime = float("%0.2f" % (sum(executionTime) / NumOfRuns))
                    avgConvergence = numpy.around(numpy.mean(convergence, axis=0, dtype=numpy.float64), decimals=2).tolist()
                    a = numpy.concatenate([[optimizerName, testfun, avgExecutionTime], avgConvergence])
                    writer.writerow(a)
                out.close()


    if Export_convergence == True:
        conv_plot.run(results_directory, optimizer, objectivefunc, Iterations)

    if Export_boxplot == True:
        box_plot.run(results_directory, optimizer, objectivefunc, Iterations)

    if Flag == False:
        print(
            "No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions"
        )

    print("Execution completed")
