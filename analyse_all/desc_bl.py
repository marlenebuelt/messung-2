import totals_bl
import pandas as pd

cpu = totals_bl.df_bl['CPU Utilization']
mem = totals_bl.df_bl['%mem']
power_total = totals_bl.df_bl['Total Power']

df_desc = pd.DataFrame([[cpu.min()*100, cpu.max()*100, cpu.mean()*100, cpu.median()*100, cpu.std()], 
                        [mem.min(), mem.max(), mem.mean(), mem.median(), mem.std()], 
                        [power_total.min(), power_total.max(), power_total.mean(), power_total.median(), power_total.std()]],
                       columns=['Minimum', 'Maximum', 'Mean', 'Median', 'Standard Deviation'], 
                       index=['CPU Utilization [%]','Memory Utilization[%]','Total Power [W]'])
print(df_desc)

df_desc.to_csv('bl_messung/df_desc')

def descdf():
    global df_desc
    return df_desc