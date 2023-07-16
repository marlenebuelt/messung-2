import pandas as pd
import totals_bl
import totals_dt
import totals_lr
import totals_svm
import totals_nn
import scipy.stats as stats
from cliffs_delta import cliffs_delta

cpu_bl = totals_bl.df_bl['CPU Utilization']
cpu_dt = totals_dt.df_dt['CPU Utilization']
cpu_lr = totals_lr.df_lr['CPU Utilization']
cpu_svm = totals_svm.df_svm['CPU Utilization']
cpu_nn = totals_nn.df_nn['CPU Utilization']

print(stats.mannwhitneyu(cpu_dt, cpu_lr).pvalue)

print(stats.mannwhitneyu(cpu_svm, cpu_nn).pvalue)

print(stats.mannwhitneyu(cpu_dt, cpu_nn).pvalue)