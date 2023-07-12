import pandas as pd
import statistics
from datetime import datetime
import methods

powerjoular_lr = pd.read_csv('2_logreg/powerjoular_lr.csv', header=None)
powerjoular_lr.columns = ['time', 'cpu_avg','Total Power', 'CPU Power', 'power_gpu']
#powerjoular_lr['time'] = pd.to_datetime(powerjoular_lr['time']).dt.strftime('%H:%M:%S')

processes_lr = pd.read_csv('2_logreg/processes_lr.csv', sep=';', header=None)
processes_lr.columns = ['time', '%CPU', '%mem']
#processes_lr['time'] = pd.to_datetime(processes_lr['time']).dt.strftime('%H:%M:%S')

runtime_logs =  pd.read_csv('2_logreg/logreg.csv', sep=';', header=None)
runtime_logs.columns = ['time', 'startstop']
runtime_logs.reset_index(drop=True, inplace=True)
runtime_logs['time'] = pd.to_datetime(runtime_logs['time']).dt.strftime('%H:%M:%S')
print(runtime_logs)
#outer join 
df_lr = pd.merge(powerjoular_lr, processes_lr, how='left', on='time')
df_lr = pd.merge(df_lr, runtime_logs, how='left', on='time')

#iterate over values to define runtimes
methods.determineRuntimePhases(df_lr)

df_lr = df_lr.dropna()
methods.avgRuntime(runtime_logs)

methods.avgMemory(df_lr)
methods.avgCPU(df_lr)
methods.avgTotalPower(df_lr)

print(df_lr)
def getdf_lr():
    global df_lr
    return df_lr