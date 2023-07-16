import pandas as pd
import totals_bl
import totals_dt
import totals_lr
import totals_svm
import totals_nn
import methods

cpu_bl = totals_bl.df_bl['CPU Utilization'].mean()
mem_bl = totals_bl.df_bl['%mem'].mean()
power_total_bl = totals_bl.df_bl['Total Power'].mean()

cpu_dt = totals_dt.df_dt['CPU Utilization'].mean()
mem_dt = totals_dt.df_dt['%mem'].mean()
power_total_dt = totals_dt.df_dt['Total Power'].mean()

cpu_lr = totals_lr.df_lr['CPU Utilization'].mean()
mem_lr = totals_lr.df_lr['%mem'].mean()
power_total_lr = totals_lr.df_lr['Total Power'].mean()

cpu_svm = totals_svm.df_svm['CPU Utilization'].mean()
mem_svm = totals_svm.df_svm['%mem'].mean()
power_total_svm = totals_svm.df_svm['Total Power'].mean()

cpu_nn = totals_nn.df_nn['CPU Utilization'].mean()
mem_nn = totals_nn.df_nn['%mem'].mean()
power_total_nn = totals_nn.df_nn['Total Power'].mean()

df_mean_abs = pd.DataFrame([[cpu_bl*100, cpu_dt*100, cpu_lr*100, cpu_svm*100, cpu_nn*100], 
                        [mem_bl, mem_dt,mem_lr, mem_svm, mem_nn], 
                        [power_total_bl, power_total_dt, power_total_lr,power_total_svm,power_total_nn]],
                    columns=['BL', 'DT', 'Log. Reg.','SVM', 'MLP'], 
                    index=['CPU Utilization [%]','Memory Utilization[%]','Total Power [W]'])

df_mean_rel = pd.DataFrame([[methods.get_change(cpu_dt, cpu_bl),
                        methods.get_change(cpu_lr, cpu_bl),
                        methods.get_change(cpu_svm, cpu_bl),
                        methods.get_change(cpu_nn, cpu_bl)], 
                        [methods.get_change(mem_dt, mem_bl),
                        methods.get_change(mem_lr, mem_bl),
                        methods.get_change(mem_svm, mem_bl),
                        methods.get_change(mem_nn, mem_bl)], 
                        [methods.get_change(power_total_dt, power_total_bl),
                        methods.get_change(power_total_lr, power_total_bl),
                        methods.get_change(power_total_svm, power_total_bl),
                        methods.get_change(power_total_nn, power_total_bl)]],
                    columns=['Delta DT %', 'Delta LogReg %', 'Delta SVM %', 'Delta MLP % '], 
                    index=['CPU Utilization [%]','Memory Utilization[%]','Total Power [W]'])

df_mean_abs.to_csv('mean_to_bl_abs.csv', float_format='%.2f')
df_mean_rel.to_csv('mean_to_bl_rel.csv', float_format='%.2f')