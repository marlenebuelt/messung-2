import pandas as pd
import statistics
import methods

powerjoular_dt = pd.read_csv('1_dt_results/powerjoular_dt.csv',header=None)
powerjoular_dt.columns = ['time', 'CPU Utilization','Total Power', 'power_cpu', 'power_gpu']

processes_dt = pd.read_csv('1_dt_results/processes_dt.csv', sep=';', header=None)
processes_dt.columns = ['time', '%CPU', '%mem']

runtime_logs =  pd.read_csv('1_dt_results/dte.csv', sep=';', header=None)
runtime_logs.columns = ['time', 'startstop']
runtime_logs.reset_index(drop=True, inplace=True)
runtime_logs['time'] = pd.to_datetime(runtime_logs['time']).dt.strftime('%H:%M:%S')

#outer join 
df_dt = pd.merge(powerjoular_dt, processes_dt, how='left', on='time')
df_dt = pd.merge(df_dt, runtime_logs, how='left', on='time')

#iterate over values to define runtimes
methods.determineRuntimePhases(df_dt)

df_dt = df_dt.dropna()
runtime = methods.avgRuntime(runtime_logs)

methods.avgMemory(df_dt)
methods.avgCPU(df_dt)
methods.avgTotalPower(df_dt)

df_dt.to_csv('1_dt_results/df_dt')