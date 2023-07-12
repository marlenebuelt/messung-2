import pandas as pd
import numpy as np

powerjoular_bl = pd.read_csv('bl_messung/powerjoular_baseline.csv', header=None)
powerjoular_bl.columns = ['time', 'cpu_avg','power_all', 'power_cpu', 'power_gpu']

processes_bl = pd.read_csv('bl_messung/processes.csv', header=None, sep=';')
processes_bl.columns = ['time', '%CPU', '%mem']

#outer join 
df_bl = pd.merge(powerjoular_bl, processes_bl, how='left', on='time')
df_bl = df_bl.dropna()
print(df_bl)
#average cpu and memory
avg_cpu = df_bl['%CPU'].mean()
avg_mem = df_bl['%mem'].mean()

#average power
avg_cpu_percentage = df_bl.loc[:, 'cpu_avg'].mean()
avg_power_all = df_bl.loc[:, 'power_all'].mean()
avg_power_cpu = df_bl.loc[:, 'power_cpu'].mean()
avg_mem = df_bl.loc[:, '%mem'].mean()

print('avg cpu %: ' + str(avg_cpu_percentage))
print('avg power all: ' + str(avg_power_all))
print('avg power cpu: ' + str(avg_power_cpu))
print('avg mem: ' + str(avg_power_cpu))
#print(df_bl)

df_bl.to_csv('df_bl.csv')