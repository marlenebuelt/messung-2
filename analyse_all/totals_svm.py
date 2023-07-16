import pandas as pd
import statistics
import methods

powerjoular_svm = pd.read_csv('3_svm/powerjoular.csv')

processes_svm = pd.read_csv('3_svm/processes_svm.csv', sep=';', header=None)
processes_svm.columns = ['time', '%CPU', '%mem']

runtime_logs =  pd.read_csv('3_svm/svm.csv', sep=';', header=None)
runtime_logs.columns = ['date','time', 'startstop']
runtime_logs.reset_index(drop=True, inplace=True)
runtime_logs['time'] = pd.to_datetime(runtime_logs['time']).dt.strftime('%H:%M:%S')

#outer join 
df_svm = pd.merge(powerjoular_svm, processes_svm, how='left', on='time')
df_svm = pd.merge(df_svm, runtime_logs, how='left', on='time')
#iterate over values to define runtimes
#df_svm = df_svm.dropna()
methods.determineRuntimePhases(df_svm)
df_svm = df_svm[['Date','time','CPU Utilization','Total Power','CPU Power','%mem','startstop']]
df_svm = df_svm.dropna()


list_runtime = []
df_length = len(df_svm)
for index, row in df_svm.iloc[::2].iterrows():
    if index + 1 < df_length:
        start = pd.Timestamp(row['Date'] + ' ' + row['time'])
        stop = pd.Timestamp(df_svm.iloc[index + 1]['Date'] + ' ' + df_svm.iloc[index + 1]['time'])

        runtime = stop - start
        runtime = runtime.total_seconds()  # Get the time difference in seconds
        list_runtime.append(runtime)
        runtime = stop - start
        runtime = runtime.total_seconds()  # Get the time difference in seconds
        list_runtime.append(runtime)

runtime_avg = statistics.mean(list_runtime)
print('avg runtime: ' + str(runtime_avg))

methods.avgMemory(df_svm)
methods.avgCPU(df_svm)
methods.avgTotalPower(df_svm)

df_svm.to_csv('3_svm/df_svm')