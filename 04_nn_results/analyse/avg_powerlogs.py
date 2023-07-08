import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('04_nn_results/powerjoular_nn.csv', header=None)
df.columns = ['timestamp', 'cpu_avg','power_all', 'power_cpu', 'power_gpu']

avg_cpu_percentage = df.loc[:, 'cpu_avg'].mean()
avg_power_all = df.loc[:, 'power_all'].mean()
avg_power_cpu = df.loc[:, 'power_cpu'].mean()

print(avg_cpu_percentage)
print(avg_power_all)
print(avg_power_cpu)

