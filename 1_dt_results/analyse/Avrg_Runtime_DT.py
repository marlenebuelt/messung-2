import pandas as pd
import statistics
from datetime import datetime

# credit to https://stackoverflow.com/questions/25055712/pandas-every-nth-row, https://stackoverflow.com/questions/22923775/calculate-time-difference-between-two-pandas-columns-in-hours-and-minutes

runtime_logs =  pd.read_csv('1_dt_results/dte.csv', sep=';', header=None)
runtime_logs.columns = ['time', 'startstop']
runtime_logs.reset_index(drop=True, inplace=True)
runtime_logs['time']= pd.to_datetime(runtime_logs['time'])
list_runtime = []

for index, row in runtime_logs.iloc[::2].iterrows():
    start = pd.Timestamp(row[0])
    stop = pd.Timestamp(runtime_logs.iloc[index + 1][0])

    runtime = stop-start
    runtime = runtime.seconds
    list_runtime.append(runtime)
runtime_avg = statistics.mean(list_runtime)
print(runtime_avg)