import pandas as pd
import totals_bl
import totals_dt
import totals_lr
import totals_svm
import totals_nn
import scipy.stats as stats
from functools import partial

cpu_bl = totals_bl.df_bl['CPU Utilization']
mem_bl = totals_bl.df_bl['%mem']
power_total_bl = totals_bl.df_bl['Total Power']

cpu_dt = totals_dt.df_dt['CPU Utilization']
mem_dt = totals_dt.df_dt['%mem']
power_total_dt = totals_dt.df_dt['Total Power']

cpu_lr = totals_lr.df_lr['CPU Utilization']
mem_lr = totals_lr.df_lr['%mem']
power_total_lr = totals_lr.df_lr['Total Power']

cpu_svm = totals_svm.df_svm['CPU Utilization']
mem_svm = totals_svm.df_svm['%mem']
power_total_svm = totals_svm.df_svm['Total Power']

cpu_nn = totals_nn.df_nn['CPU Utilization']
mem_nn = totals_nn.df_nn['%mem']
power_total_nn = totals_nn.df_nn['Total Power']



df_significance = pd.DataFrame([[stats.mannwhitneyu(cpu_bl, cpu_dt).pvalue, 
                        stats.mannwhitneyu(cpu_bl, cpu_lr).pvalue,
                        stats.mannwhitneyu(cpu_bl, cpu_svm).pvalue,
                        stats.mannwhitneyu(cpu_bl, cpu_nn).pvalue], 
                        [stats.mannwhitneyu(mem_bl, mem_dt).pvalue,
                        stats.mannwhitneyu(mem_bl, mem_lr).pvalue,
                        stats.mannwhitneyu(mem_bl, mem_svm).pvalue,
                        stats.mannwhitneyu(mem_bl, mem_nn).pvalue], 
                        [stats.mannwhitneyu(power_total_bl, power_total_dt).pvalue,
                        stats.mannwhitneyu(power_total_bl, power_total_lr).pvalue,
                        stats.mannwhitneyu(power_total_bl, power_total_svm).pvalue,
                        stats.mannwhitneyu(power_total_bl, power_total_nn).pvalue]],
                    columns=['DT', 'LogReg','SVM', 'MLP'],      
                    index=['CPU Utilization [%]','Memory Utilization[%]','Total Power [W]'])


pd.set_option('float_format', lambda x: '%.3f' % x)

print(df_significance)
df_significance.to_csv('df_significance.csv', float_format='%.3f')