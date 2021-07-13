import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv(r"C:\Users\phamv\Downloads\MAS_PROJECT\01_DATA\D11_Science_and_Technology\03_Patents.csv")
def chooseData(fea, limit, x_name, y_name):
    data=[]
    x=[]
    y=[]
    for row in df.iterrows():

        if row[1][fea] == limit :
            x.append(row[1][x_name])
            y.append(row[1][y_name])
    data.append(x)
    data.append(y)
    return data

# ten column muon chon vi du nhu : ten nuoc, ten luc dia ...
print("Ten column muon chon:")
fea = input()
# gia tri cua column minh muon chon vi du nhu Japan, China, ...
print("Gia tri cua column: ")
limit = input()
# column minh muon du doan x
print("Dau vao x:")
x = input()
# column minh muon du doan y
print("Phan muon du doan:")
y = input()

#tap du lieu x, y
data = chooseData(fea, limit, x, y)
x_data = np.array(data[0]).reshape(-1,1)
y_data = np.array(data[1])
model = LinearRegression()
model.fit(x_data, y_data)
r_sq = model.score(x_data, y_data)
print('Coefficient of determination:', r_sq)
print("Nhap dau vao x:")
x_input = float(input())
x_arr = np.array(x_input).reshape(-1, 1)
y_pred = model.predict(x_arr)
print("Du doan: "+ str(round(y_pred[0], 0)))


