from math import sqrt
from numpy import mean
from scipy.stats import ttest_ind
import pandas as pd
import numpy as np

data = pd.read_csv('website_ab_test.csv')
metrics = ['Click Through Rate','Conversion Rate', 'Bounce Rate']
themes = ['Light Theme', 'Dark Theme']
#loop through each metric
for metric in metrics:
    print('Metric: ', metric)

    #loop through each theme
    for i in range(len(themes)):
        for j in range(i+1, len(themes)):
            theme1 = themes[i]
            theme2 = themes[j]

            #calculate the mean and standard deviation  for each theme
            mean1 = mean(data[data['Theme'] == theme1][metric])
            mean2 = mean(data[data['Theme'] == theme2][metric])
            std1 = np.std(data[data['Theme'] == theme1][metric])
            std2 = np.std(data[data['Theme'] == theme2][metric])

            #calculate the t-statistic and pvalue for the two groupd
            n1 = len(data[data['Theme'] == theme1][metric])
            n2 = len(data[data['Theme'] == theme2][metric])
            dof = n1 + n2 - 2
            pooled_std = sqrt(((n1-1)*(std1**2) + (n2-1)*(std2**2))/dof)
            t_stat =(mean1-mean2)/ (pooled_std * sqrt(1/n1 + 1/n2))
            p_val = 2 * (1 - ttest_ind(data[data['Theme'] == theme1][metric],\
                                        data[data['Theme'] == theme2][metric]).pvalue)

            #calculate the effect size (Cohen's d)
            effect_size = (mean1-mean2)/ pooled_std
            #print the results for the two groups
            print(theme1, 'vs', theme2)
            print('Mean:', theme1, ':', mean1)
            print('Mean:', theme2, ':', mean2)
            print('Standard Deviation:', theme1, ':', std1)
            print('Standard Deviation:', theme2, ':', std2)
            print('T-statistic:', t_stat)
            print('P-value:', p_val)
            print('Effect Size (Cohen\'s d):', effect_size)
            print()