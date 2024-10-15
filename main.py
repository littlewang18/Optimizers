from optimizer import run
import os
# import psutil

'''群智算法'''
optimizer = ["GWO"]
# "DE", "MFO", "MVO", "PSO", "WOA", "CS", "GWO", "SSA", "HSSA"

# 1初始化， -> 2. 适应度计算， 标记  ->3. 位置更新 1.流淌（跟着最优的洼地）2. 蒸发（70%， 重新位置 -》 没有洼地的地方（适应度值未知的地方） 3. 下雨 -》 ）
'''优化函数'''
objectivefunc = ["F1"]
# "F1", "F2", "F3", "F4", "F5","F6", "F7", "F8", "F9", "F10",
# "F11", "F12","F13", "F14", "F15","F16", "F17", "F18", "F19", "F20","F21""F22","F23"
# "ker"

'''运行次数'''
NumOfRuns = 1
# 30

'''初始化参数'''
params = {"PopulationSize":50, "Iterations": 100}


'''数据保存'''
export_flags = {
    "Export_avg": True,
    "Export_details": True,
    "Export_convergence": True,
    "Export_boxplot": True,
}

run(optimizer, objectivefunc, NumOfRuns, params, export_flags)