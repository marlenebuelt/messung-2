import pandas as pd
from scipy import stats
from scipy.stats import mannwhitneyu
import totals_nn
import totals_bl
from scipy.stats import ttest_ind

df_bl = totals_bl.df_bl
df_nn = totals_nn.df_nn

print(df_bl)
print(df_nn)
#t-test
cpu_ttest = ttest_ind(df_bl['cpu_avg'],df_nn['CPU Utilization'])
print(cpu_ttest)

power_total_ttest = ttest_ind(df_bl['power_all'],df_nn['Total Power'])
print(power_total_ttest)

mem_ttest = ttest_ind(df_bl['%mem'],df_nn['%mem'])
print(mem_ttest)
