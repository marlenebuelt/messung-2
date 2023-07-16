import pandas as pd
import methods

powerjoular_bl = pd.read_csv('bl_messung/powerjoular_baseline.csv', header=None)
powerjoular_bl.columns = ['time', 'CPU Utilization','Total Power', 'power_cpu', 'power_gpu']

processes_bl = pd.read_csv('bl_messung/processes.csv', header=None, sep=';')
processes_bl.columns = ['time', '%CPU', '%mem']

#outer join 
df_bl = pd.merge(powerjoular_bl, processes_bl, how='left', on='time')
df_bl = df_bl.dropna()
print(df_bl)

df_bl = df_bl.dropna()

methods.avgMemory(df_bl)
methods.avgCPU(df_bl)
methods.avgTotalPower(df_bl)

df_bl.to_csv('bl_messung/df_bl')
def df():
    global df_bl
    return df_bl