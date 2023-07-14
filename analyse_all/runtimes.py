import pandas as pd
import totals_bl
import totals_dt
import totals_lr
import totals_svm
import totals_nn
import methods

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
