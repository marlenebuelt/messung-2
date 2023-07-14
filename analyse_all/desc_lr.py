import totals_lr
import pandas as pd

cpu = totals_lr.df_lr['CPU Utilization']
mem = totals_lr.df_lr['%mem']
power_total = totals_lr.df_lr['Total Power']

df_desc = pd.DataFrame([[cpu.min()*100, cpu.max()*100, cpu.mean()*100, cpu.median()*100, cpu.std()], 
                        [mem.min(), mem.max(), mem.mean(), mem.median(), mem.std()], 
                        [power_total.min(), power_total.max(), power_total.mean(), power_total.median(), power_total.std()]],
                       columns=['Minimum', 'Maximum', 'Mean', 'Median', 'Standard Deviation'], 
                       index=['CPU Utilization [%]','Memory Utilization[%]','Total Power [W]'])


print(df_desc)

df_desc.to_csv('2_logreg/df_desc_lr')
def descdf():
    global df_desc
    return df_desc