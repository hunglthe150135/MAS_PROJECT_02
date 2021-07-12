import pandas as pd
from math import sqrt
import numpy as np
from scipy.stats import chisquare
from scipy import stats
from scipy.stats import chi2_contingency

data = pd.read_csv(r'US_2017_GRADUATION_RATE.csv')
df = pd.DataFrame(data, columns=['gender','race/ethnicity','parental level of education','parental income','test preparation course','ACT composite score','SAT total score','high school gpa','college gpa','years to graduate'])

total = df['years to graduate'].sum(axis = 0)
sample_size = df['years to graduate'].count()
sample_mean = total/(sample_size - 1)
population_mean = total/sample_size
t_dis = abs(stats.t.ppf(0.025,sample_size - 1))

def a():
    print("Sample Mean: ")
    print(np.mean(df['years to graduate']))
    print("Sample standard deviation: ")
    print(df['years to graduate'].std())
    print("Sample size: ")
    print(sample_size)
    print("t-distribution")
    print(t_dis)

    print("Result:")

    print((sample_mean - t_dis) * (sample_stdv / np.sqrt(sample_size)))

    print((sample_mean + t_dis) * (sample_stdv / np.sqrt(sample_size)))

df['Deviation'] = (df['years to graduate'] - sample_mean)*(df['years to graduate'] - sample_mean)
variance  = (df['Deviation'].sum(axis = 0) / (sample_size - 1))
sample_stdv = np.sqrt(variance)

def b():
    print("Variance:")
    print(variance)
    print(str((sample_size - 1) * variance / stats.chi2.ppf(q=1 - 0.05, df=999)) + " <= u <= " + str(
        (sample_size - 1) * variance / stats.chi2.ppf(q=0.05, df=999)))

