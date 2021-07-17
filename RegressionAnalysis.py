import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr
import math


data = pd.read_csv(open(r'C:\Users\phamv\PycharmProjects\pythonProject\MAS_PROJECT_02\US_2017_GRADUATION_RATE.csv', encoding= "utf8"))

def calBasic(col, df):
    total = df[col].sum(axis=0)
    sample_size = df[col].count()
    sample_mean = total / (sample_size - 1)
    sample_std = df[col].std()
    population_mean = total/ sample_size

    return [total, sample_size, sample_mean, sample_std, population_mean]

def calHypo(ox_name, oy_name,ox, oy, df):
    ox_val = calBasic(ox_name, df)
    oy_val = calBasic(oy_name, df)

    Sxx= 0
    for x in ox:
        Sxx = Sxx + math.pow(x, 2)
    Sxx = Sxx - ox_val[1] * math.pow(ox_val[2], 2)
    print("Sxx :" +str(Sxx))
    SSt = 0
    for y in oy:
        SSt = SSt + math.pow(y, 2)
    SSt = SSt - oy_val[1] * math.pow(oy_val[2], 2)
    print("SSt :" + str(SSt))

    Sxy = 0
    for val in range(len(ox)):
        Sxy = Sxy + ox[val]*oy[val]
    Sxy = Sxy - ox_val[1]*ox_val[2]*oy_val[2]
    print("Sxy :" + str(Sxy))

    B1 = Sxy/Sxx
    print("B1 :"+ str(B1))

    SSe = SSt-B1*Sxy
    print("SSe :" + str(SSe))

    std_sqr = SSe/(ox_val[2]-2)
    print("std_sqr :" + str(std_sqr))

    se = math.sqrt(std_sqr/Sxx)
    print("se :"+str(se))

    return [Sxx, Sxy, B1, SSt, SSe, std_sqr, se]


# SAT -> ACT
SAT=[]
ACT=[]
for row in data.iterrows():
    SAT.append(row[1]['SAT total score'])
    ACT.append(row[1]['ACT composite score'])

#Hypothesis
hyp_SAT=calHypo('SAT total score', 'ACT composite score', SAT, ACT, data)


#Correlation Coefficent of SAT vs ACT

stat, p = pearsonr(SAT, ACT)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')

model_SAT = LinearRegression()
model_SAT.fit(np.array(SAT).reshape(-1, 1), ACT)


plt.scatter(SAT, ACT, color = "red")
plt.plot(SAT, model_SAT.predict(np.array(SAT).reshape(-1, 1)), color = "green")
plt.title("SAT to ACT")
plt.xlabel("SAT")
plt.ylabel("ACT")
plt.show()

print("============================================================================")
#Years to graduate -> College gpa
ytg = []
gpa = []
for row in data.iterrows():
    ytg.append(row[1]['years to graduate'])
    gpa.append(row[1]['college gpa'])

#Hypothesis
hyp_GPA=calHypo('years to graduate', 'college gpa', ytg, gpa, data)

model_GPA = LinearRegression()
model_GPA.fit(np.array(ytg).reshape(-1, 1), gpa)



#Correlation Coefficent of YTG vs GPA

stat_GPA, p_GPA = pearsonr(ytg, gpa)
print('stat=%.3f, p=%.3f' % (stat_GPA, p_GPA))
if p_GPA > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')

model_SAT = LinearRegression()
model_SAT.fit(np.array(SAT).reshape(-1, 1), ACT)

plt.scatter(ytg, gpa, color="red")
plt.plot(ytg, model_GPA.predict(np.array(ytg).reshape(-1, 1)), 1, color="green")
plt.title("years to graduate to college gpa")
plt.xlabel("years to graduate")
plt.ylabel("college gpa")
plt.show()

