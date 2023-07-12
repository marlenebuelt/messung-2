import pandas as pd
from scipy import stats
import totals_dt
import totals_bl
from scipy.stats import ttest_ind

df_bl = totals_bl.df_bl
df_dt = totals_dt.df_dt

print(df_bl)
print(df_dt)
#t-test
cpu_ttest = ttest_ind(df_bl['cpu_avg'],df_dt['CPU Utilization'])
print(cpu_ttest)

power_total_ttest = ttest_ind(df_bl['power_all'],df_dt['Total Power'])
print(power_total_ttest)

mem_ttest = ttest_ind(df_bl['%mem'],df_dt['%mem'])
print(mem_ttest)
