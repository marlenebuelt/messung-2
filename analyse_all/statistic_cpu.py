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

groups_cpu = [cpu_bl, cpu_dt, cpu_lr, cpu_svm, cpu_nn]

results_cpu = pd.DataFrame(columns=['Base', 'Comparison Group', 'Mann-Whitney U Statistic',
                                    'Mann-Whitney U p-value', 'Cliffs Delta'])

for i in range(len(groups_cpu)):
    base = groups_cpu[i]
    base_name = [k for k, v in locals().items() if v is base][0]
    
    for j in range(i+1, len(groups_cpu)):
        comparison = groups_cpu[j]
        comparison_name = [k for k, v in locals().items() if v is comparison][0]
        print('Comparison group:', comparison_name)
        
        common_cols = list(set(base.index).intersection(comparison.index))
        
        base_common = base.reindex(common_cols)
        comparison_common = comparison.reindex(common_cols)

        mannwhitney_result = stats.mannwhitneyu(base_common, comparison_common)
        cliffs_delta_result = cliffs_delta(base_common, comparison_common)[0]
        
        results_cpu = results_cpu.append({'Base': base_name,
                                          'Comparison Group': comparison_name,
                                          'Mann-Whitney U Statistic': mannwhitney_result.statistic,
                                          'Mann-Whitney U p-value': mannwhitney_result.pvalue,
                                          'Cliffs Delta': cliffs_delta_result}, ignore_index=True)

print(results_cpu)
