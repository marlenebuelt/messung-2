import pandas as pd
import totals_lr
from scipy.stats import ttest_ind

df_bl = pd.read_csv('bl_messung/df_bl.csv')
df_lr = totals_lr.df_lr

#t-test
cpu_ttest = ttest_ind(df_lr['cpu_avg'],df_bl['cpu_avg'],equal_var=False)
print('cpu_ttest' + str(cpu_ttest))

power_total_ttest = ttest_ind(df_lr['power_all'],df_bl['power_all'])
print('power_total_ttest' + str(power_total_ttest))

power_cpu_ttest = ttest_ind(df_lr['power_cpu'],df_bl['power_cpu'])
print('power_cpu_ttest'+ str(power_cpu_ttest))

mem_ttest = ttest_ind(df_lr['%mem'], df_bl['%mem'])
print('mem_ttest'+str(mem_ttest))
