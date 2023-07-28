# Software-based Measurement
This is a repository of all data I collected for the software-based measurements for my bachelor's thesis as well as analysis files used for interpretation and discussion. 
For these measurements, the [PowerJoular](https://joular.github.io/powerjoular/) tool is used.

All measurement files are found in the corresponding folders:
powerjoular_[model].csv - Power utilization log 
processes_[model].log - Log of memory utilization 
[model].csv - runtime logs 

## /
[model].py - execution of the model / starts a prediction

## /analyse_all
totals_[model].py - merge of the collected files and data, cleaning of data of the respective models 
desc_[model].py - descriptive variables of all models
mean_to_bl.py - Relative comparison to baseline data
methods.py - service class to store all methods used in separate analysis files
mwu.ipynb - Significance tests and effect size test (Mann-Whitney-U and Cliff's delta)
shapiro_wilk.ipynb - Shapiro-Wilk-Test for normality