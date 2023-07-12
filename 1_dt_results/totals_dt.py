import pandas as pd
import statistics
from scipy.stats import mannwhitneyu

powerjoular_dt = pd.read_csv('1_dt_results/powerjoular_dt.csv',header=None)
powerjoular_dt.columns = ['time', 'cpu_avg','power_all', 'power_cpu', 'power_gpu']

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
fill_value = 'runtime'
start_index = None

for index, row in df_dt.iterrows():
    if row['startstop'] == 'Start':
        start_index = index
    elif row['startstop'] == 'Stop' and start_index is not None:
        df_dt.loc[start_index:index, 'startstop'] = fill_value
        start_index = None

df_dt = df_dt.dropna()

#average runtime
list_runtime = []
for index, row in runtime_logs.iloc[::2].iterrows():
    start = pd.Timestamp(row[0])
    stop = pd.Timestamp(runtime_logs.iloc[index + 1][0])

    runtime = stop-start
    runtime = runtime.seconds
    list_runtime.append(runtime)
runtime_avg = statistics.mean(list_runtime)
print('avg runtime: '+str(runtime_avg))

#average cpu and memory
avg_cpu = df_dt.loc[:, '%CPU'].mean()
avg_mem = df_dt.loc[:, '%mem'].mean()

print('avg_cpu: ' + str(avg_cpu))
print('avg_mem: ' + str(avg_mem))

#average power
avg_cpu_percentage = df_dt.loc[:, 'cpu_avg'].mean()
avg_power_all = df_dt.loc[:, 'power_all'].mean()
avg_power_cpu = df_dt.loc[:, 'power_cpu'].mean()

print('avg cpu %: ' + str(avg_cpu_percentage))
print('avg power all: ' + str(avg_power_all))
print('avg power cpu: ' + str(avg_power_cpu))
#print(df_dt)
df_dt.to_csv('1_dt_results/df_dt.csv')
def getDf_dt():
    global df_dt
    return df_dt