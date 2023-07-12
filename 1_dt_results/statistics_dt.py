import pandas as pd
import totals_dt
from scipy.stats import ttest_ind

df_bl = pd.read_csv('bl_messung/df_bl.csv')
df_dt = totals_dt.df_dt

#t-test
cpu_ttest = ttest_ind(df_dt['cpu_avg'],df_bl['cpu_avg'],equal_var=False)
print('cpu_ttest' + str(cpu_ttest))

power_total_ttest = ttest_ind(df_dt['power_all'],df_bl['power_all'])
print('power_total_ttest' + str(power_total_ttest))

power_cpu_ttest = ttest_ind(df_dt['power_cpu'],df_bl['power_cpu'])
print('power_cpu_ttest'+ str(power_cpu_ttest))

mem_ttest = ttest_ind(df_dt['%mem'], df_bl['%mem'])
print('mem_ttest'+str(mem_ttest))
