
import pandas as pd
import math
from scipy import stats
from statsmodels.stats import weightstats as stests

df = pd.read_csv("US_2017_GRADUATION_RATE.csv")
print("Hypothesis mean: ")
hyp_mean = float(input())
total = df['years to graduate'].sum(axis = 0)
sample_size = df['years to graduate'].count()
sample_mean = total/(sample_size - 1)
sample_std = df['years to graduate'].std()
population_mean = total/sample_size
t_stat = (sample_mean-hyp_mean)/(sample_std/math.sqrt(sample_size))
p_value = stats.t.sf(t_stat, df=sample_size-1)

print("3.a :")
print("Sample Mean: "+str(sample_mean))
print("Sample standard deviation: "+ str(sample_std))
print("Sample size: "+str(sample_size))
print("Test statistic :"+str(t_stat))
print("P value of Mean:"+str(p_value))


print("3.b :")
print("Hypothesis p : ")
p0 = float(input())
count=0
for row in df.iterrows():
    if(row[1]['gender']=='male'):
        count =count+1
t_stat_p = (count-sample_size*p0)/(math.sqrt(sample_size*p0*(1-p0)))
p_value_p = stats.norm.sf(abs(t_stat_p))

print("Number of Male: "+str(count))
print("Sample size :"+ str(sample_size))
print("Test statistic :"+ str(t_stat_p))
print("P-value of Propotion:"+ str(p_value_p))








