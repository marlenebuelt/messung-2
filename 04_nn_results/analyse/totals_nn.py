import pandas as pd
import statistics
import numpy as np

powerjoular_nn = pd.read_csv('04_nn_results/powerjoular_nn.csv', header=None)
powerjoular_nn.columns = ['time', 'cpu_avg','power_all', 'power_cpu', 'power_gpu']

processes_nn = pd.read_csv('04_nn_results/processes_nn.csv', sep=';', header=None)
processes_nn.columns = ['time', '%CPU', '%mem']

runtime_logs =  pd.read_csv('04_nn_results/nn.csv', sep=';', header=None)
runtime_logs.columns = ['time', 'startstop']
runtime_logs.reset_index(drop=True, inplace=True)
runtime_logs['time'] = pd.to_datetime(runtime_logs['time']).dt.strftime('%H:%M:%S')

#outer join 
df_nn = pd.merge(powerjoular_nn, processes_nn, how='left', on='time')
df_nn = pd.merge(df_nn, runtime_logs, how='left', on='time')

#iterate over values to define runtimes
fill_value = 'runtime'
start_index = None

for index, row in df_nn.iterrows():
    if row['startstop'] == 'Start':
        start_index = index
    elif row['startstop'] == 'Stop' and start_index is not None:
        df_nn.loc[start_index:index, 'startstop'] = fill_value
        start_index = None

df_nn = df_nn.drop(df_nn[df_nn['startstop'] == 'NaN'].index)

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
avg_cpu = processes_nn.loc[:, '%CPU'].mean()
avg_mem = processes_nn.loc[:, '%mem'].mean()

print('avg_cpu: ' + str(avg_cpu))
print('avg_mem: ' + str(avg_mem))

#average power
avg_cpu_percentage = powerjoular_nn.loc[:, 'cpu_avg'].mean()
avg_power_all = powerjoular_nn.loc[:, 'power_all'].mean()
avg_power_cpu = powerjoular_nn.loc[:, 'power_cpu'].mean()

print('avg cpu %: ' + str(avg_cpu_percentage))
print('avg power all: ' + str(avg_power_all))
print('avg power cpu: ' + str(avg_power_cpu))
print(df_nn)