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

df_mean = pd.DataFrame([[cpu_bl*100, 
                        cpu_dt*100, methods.get_change(cpu_dt, cpu_bl),
                        cpu_lr*100, methods.get_change(cpu_lr, cpu_bl),
                        cpu_svm*100, methods.get_change(cpu_svm, cpu_bl),
                        cpu_nn*100, methods.get_change(cpu_nn, cpu_bl)], 
                        [mem_bl, 
                        mem_dt, methods.get_change(mem_dt, mem_bl),
                        mem_lr, methods.get_change(mem_lr, mem_bl),
                        mem_svm, methods.get_change(mem_svm, mem_bl),
                        mem_nn, methods.get_change(mem_nn, mem_bl)], 
                        [power_total_bl, 
                        power_total_dt, methods.get_change(power_total_dt, power_total_bl),
                        power_total_lr, methods.get_change(power_total_lr, power_total_bl),
                        power_total_svm, methods.get_change(power_total_svm, power_total_bl),
                        power_total_nn, methods.get_change(power_total_nn, power_total_bl)]],
                    columns=['BL', 'DT', 'Delta DT %', 'Log. Reg.', 'Delta LogReg %','SVM', 'Delta SVM %', 
                                'MLP', 'Delta MLP % '], 
                    index=['CPU Utilization [%]','Memory Utilization[%]','Total Power [W]'])


print(df_mean)
df_mean.to_csv('mean_to_bl.csv')
print(df_mean.to_latex)
