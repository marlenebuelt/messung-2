import pandas as pd
import statistics

#iterate over values to define runtimes
def determineRuntimePhases(df):
    start_index = None
    value = 'runtime'
    for index, row in df.iterrows():
        if row['startstop'] == 'Start':
            start_index = index
        elif row['startstop'] == 'Stop' and start_index is not None:
            df.loc[start_index:index, 'startstop'] = value
            start_index = None

def dropna(df):
    df.dropna

def avgRuntime(runtime_logs):
    list_runtime = []
    for index, row in runtime_logs.iloc[::2].iterrows():
        start = pd.Timestamp(row[0])
        stop = pd.Timestamp(runtime_logs.iloc[index + 1][0])

        runtime = stop-start
        runtime = runtime.seconds
        list_runtime.append(runtime)
    runtime_avg = statistics.mean(list_runtime)
    return runtime_avg

def avgMemory(df):
    avg_mem = df.loc[:, '%mem'].mean()
    print('avg_mem: ' + str(avg_mem))

def avgTotalPower(df):
    avg_power_all = df.loc[:, 'Total Power'].mean()
    print('Total Power avg: ' + str(avg_power_all))

def avgCPU(df):
    avg_cpu_percentage = df.loc[:, 'CPU Utilization'].mean()
    print('avg cpu %: ' + str(avg_cpu_percentage))

#method: credit to https://stackoverflow.com/questions/30926840/how-to-check-change-between-two-values-in-percent#:~:text=If%20you%20want%20the%20percentage,%2Fprevious)*100%20%2D%20100%20.
def get_change(model_value, baseline_value):
    if model_value == baseline_value:
        return 0
    try:
        return (abs(model_value - baseline_value) / baseline_value) * 100.0
    except ZeroDivisionError:
        return float('inf')