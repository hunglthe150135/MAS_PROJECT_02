
import pandas as pd
import math
from scipy import stats
import numpy as np

df = pd.read_csv("US_2017_GRADUATION_RATE.csv")
total = df['years to graduate'].sum(axis = 0)
sample_size = df['years to graduate'].count()
sample_mean = total/(sample_size - 1)
sample_std = df['years to graduate'].std()
population_mean = total/sample_size


print("3.a :")
print("Hypothesis mean: ")
hyp_mean = float(input())
t_stat = (sample_mean-hyp_mean)/(sample_std/math.sqrt(sample_size))
p_value = stats.t.sf(t_stat, df=sample_size-1)

print("Sample Mean: "+str(sample_mean))
print("Sample standard deviation: "+ str(sample_std))
print("Sample size: "+str(sample_size))
print("Test statistic :"+str(t_stat))
print("P value of Mean:"+str(p_value))

print("============================================================")
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

print("============================================================")
print("4.a")
alpha = float(input())
def mean_cal(gender):
    total = 0
    amount = 0
    var = 0
    res = []
    for row in df.iterrows():
        if row[1]['gender']==gender:
            total = total + row[1]["years to graduate"]
            amount = amount +1

    res.append(amount)
    res.append(round(total/amount, 2))
    return res

def cal_var(lst, gender):
    vari = 0
    for row in df.iterrows():
        if row[1]['gender']==gender:
            vari = vari + math.pow(row[1]["years to graduate"]-lst[1], 2)

    return round(vari, 2)

mal =  mean_cal("male" )
mal.append(cal_var(mal, "male"))
fem = mean_cal("female")
fem.append(cal_var(fem, "female"))
dof = round((math.pow(mal[2]/mal[0]+fem[2]/fem[0], 2))/(math.pow(mal[2]/mal[0], 2)/(mal[0]-1)+math.pow(fem[2]/fem[0], 2)/(fem[0]-1)), 2)

print("Sample mean : Male ="+ str(mal[1])+" | "+"Female ="+str(fem[1]))
print("Sample size : Male ="+ str(mal[0])+" | "+"Female ="+str(fem[0]))
print("Varience : Male ="+ str(mal[2])+" | "+"Female ="+str(fem[2]))
print("Degree of Freedom : "+ str(dof))
# calculate t-dis
t_dis= stats.t.ppf(1-alpha/2, df=dof)
print("t-distribution :"+str(round(t_dis, 7)))
std = math.sqrt(mal[2]/mal[0]+fem[2]/fem[0])
print(str(mal[1]-fem[1]-t_dis*std)+" <= µ1 −µ2 <= "+ str(mal[1]-fem[1]+t_dis*std))

print("============================================================")
print("4.b")

def sample_pro(lst, gender):
    amount = 0
    for row in df.iterrows():
        if row[1]['gender'] == gender:
            if row[1]['test preparation course'] == 'completed':
                amount = amount+1
    res = []
    res.append(amount)
    res.append(round(amount/lst[0], 5))
    return  res

mal_pro = sample_pro(mal, 'male')
fem_pro = sample_pro(fem, 'female')
total_sample_pro = round((mal_pro[0]+fem_pro[0])/(mal_pro[1]+fem_pro[1]), 2)
z=round(stats.norm.ppf(1-alpha/2), 5)
std_pro= math.sqrt((mal_pro[1]*(1-mal_pro[1]))/mal_pro[0]+(fem_pro[1]*(1-fem_pro[1]))/fem_pro[0])

print("Sample propotion : "+ str(total_sample_pro))
print("Male completed test SS :" + str(mal_pro[1]))
print("Female completed test SS :" + str(fem_pro[1]))
print("Standard Normal Distribution: "+ str(z))
print(str(round(mal_pro[1]-fem_pro[1]-z*std_pro, 5))+" <= p1 − p2 <= " +str(round(mal_pro[1]-fem_pro[1]+z*std_pro, 5)))

print("============================================================")
print("4.c")
print("Hypothesis mean diff :")
mean_diff = float(input())
test_stat_2m  =  (mal[1]-fem[1]-mean_diff)/(math.sqrt(mal[2]/mal[0]+fem[2]/fem[0]))
p_value_p = 2*(stats.norm.sf(abs(test_stat_2m)))
print(test_stat_2m)
print(p_value_p)

print("============================================================")
print("4.d")
pool_pro = (mal_pro[0]+fem_pro[0])/(mal[0]+fem[0])
test_stat_2p = (mal_pro[1]-fem_pro[1])/(math.sqrt(pool_pro*(1-pool_pro)*(1/mal[0]+1/fem[0])))
p_value_2p = (1-round( stats.norm.sf(abs(test_stat_2p)), 5))
print(pool_pro)
print(test_stat_2p)
print(p_value_2p)