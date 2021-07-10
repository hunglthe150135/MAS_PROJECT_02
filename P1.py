import csv
import matplotlib.pyplot as plt

data1 = csv.reader(open(r'.\US_2017_GRADUATION_RATE.csv'))
def parIn(income,data):
    values = []
    count=0
    data = csv.reader(open(r'.\US_2017_GRADUATION_RATE.csv'))
    for row in data:
        if row[3] == income:
            values.append(row[3])
            count+=1
    return count
lst_income = ['0-730','730-25000','25000-50000','50000-68000','68000-90000','90000+']
lst_1 = parIn('730-25000',data1)
lst_0 = parIn('0-730',data1)
lst_2 = parIn('25000-50000',data1)
lst_3 = parIn('50000-68000',data1)
lst_4 = parIn('68000-90000',data1)
lst_5 = parIn('90000+',data1)
lst_all = lst_0,lst_1,lst_2,lst_3,lst_4,lst_5
print(lst_all)
plot = plt.bar(lst_income,lst_all)
plt.xlabel('Parental Income')
plt.ylabel('Frequency')
for value in plot:
    height = value.get_height()
    plt.text(value.get_x() + value.get_width()/2.,
             1.002*height,'%d' % float(height), ha='center', va='bottom')
plt.show()

def actAndSat(tpc,data):
    data = csv.reader(open(r'.\US_2017_GRADUATION_RATE.csv'))
    values1 = []
    values2 = []
    values = []
    for row in data:
        if row[4] == tpc:
            values1.append(int(row[5]))
            values2.append(int(row[6]))
    values.append(values1)
    values.append(values2)
    return values
lst_none = actAndSat('none',data1)
lst_completed = actAndSat('completed',data1)
lst_all_act = lst_none[0],lst_completed[0]
plt.boxplot(lst_all_act,patch_artist=True,labels=['None','Completed'])
plt.xlabel('Test preparation course')
plt.ylabel('ACT composite score')
plt.show()
lst_all_sat = lst_none[1],lst_completed[1]
plt.boxplot(lst_all_sat,patch_artist=True,labels=['None','Completed'])
plt.xlabel('Test preparation course')
plt.ylabel('SAT total score')
plt.show()