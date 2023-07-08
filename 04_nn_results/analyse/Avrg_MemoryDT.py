import pandas as pd

df = pd.read_csv('1_dt_results/processes_dt.csv', sep=';', header=None)

df.columns = ['time', '%CPU', '%mem']

avg_cpu = df.loc[:, '%CPU'].mean()
avg_mem = df.loc[:, '%mem'].mean()

print(avg_cpu)
print(avg_mem)
