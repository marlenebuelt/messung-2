import pandas as pd
import statistics
import numpy as np
import methods

powerjoular_nn = pd.read_csv('04_nn_results/powerjoular_nn.csv', header=None)
powerjoular_nn.columns = ['time', 'CPU Utilization','Total Power', 'power_cpu', 'power_gpu']

processes_nn = pd.read_csv('04_nn_results/processes_nn.csv', sep=';', header=None)
processes_nn.columns = ['time', '%CPU', '%mem']

runtime_logs =  pd.read_csv('04_nn_results/nn.csv', sep=';', header=None)
runtime_logs.columns = ['time', 'startstop']
runtime_logs.reset_index(drop=True, inplace=True)
runtime_logs['time'] = pd.to_datetime(runtime_logs['time']).dt.strftime('%H:%M:%S')

#outer join 
df_nn = pd.merge(powerjoular_nn, processes_nn, how='left', on='time')
df_nn = pd.merge(df_nn, runtime_logs, how='left', on='time')

methods.determineRuntimePhases(df_nn)

df_nn = df_nn.dropna()
methods.avgRuntime(runtime_logs)

methods.avgMemory(df_nn)
methods.avgCPU(df_nn)
methods.avgTotalPower(df_nn)

print(df_nn)

def getdf_nn():
    global df_nn
    return df_nn