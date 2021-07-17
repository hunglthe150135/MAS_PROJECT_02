import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math 

def analyse(xs, ys):
    avg_x = 0
    avg_y = 0
    sxx = 0
    sst = 0
    sxy = 0
    n = len(xs)

    for i in range(n):
        avg_x += xs[i]
        avg_y += ys[i]
        sxx += math.pow(xs[i], 2)
        sst += math.pow(ys[i], 2)
        sxy += xs[i]*ys[i]
    avg_x /= n
    avg_y /= n
    sxx = sxx - n*math.pow(avg_x, 2)
    sst = sst - n*math.pow(avg_y, 2)
    sxy = sxy - n*avg_x*avg_y

    b1 = sxy/sxx
    sse = sst - b1*sxy
    var = sse/(n-2)
    se_b1 = math.sqrt(var/sxx)

    test_statistic = b1/se_b1
    coefficient = sxy/math.sqrt(sxx*sst)

    b0 = avg_y - b1*avg_x
    return [b0, b1, test_statistic, coefficient]

def regressionModel(xs, ys, title, xlabel, ylabel, picName):
    x = np.array(xs).reshape((-1, 1))
    y = np.array(ys)
    model = LinearRegression().fit(x, y)
    plt.scatter(x, y, color = "black")
    plt.plot(x, model.predict(x), color = "blue")
    figure = plt.gcf()
    figure.set_size_inches(15, 10)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(picName)
    plt.show()

data = pd.read_csv(open(r'US_2017_GRADUATION_RATE.csv', encoding= "utf8"))
dataSat = []
dataAct = []
dataYears = []
dataGpa = []
for row in data.iterrows():
    dataSat.append(row[1]['SAT total score'])
    dataAct.append(row[1]['ACT composite score'])
    dataYears.append(row[1]['years to graduate'])
    dataGpa.append(row[1]['college gpa'])

regressionModel(dataSat, dataAct, "Regression of SAT score to ACT score", "SAT total score", "ACT composite score", "Regression of SAT to ACT")
regressionModel(dataSat, dataAct, "Regression of studying time to GPA", "years to graduate", "college gpa", "Regression of studying time to GPA")

