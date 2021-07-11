import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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
plt.xticks(rotation = 8)
plt.savefig('fig1.png')
plt.show()

def actAndSat(data):
    data = csv.reader(open(r'.\US_2017_GRADUATION_RATE.csv'))
    # values1 = []
    # values2 = []
    values = []
    for row in data:
        if row[4] == 'none' or row[4] == 'completed':
            values.append((row[4],int(row[5]),int(row[6])))
            # values2.append(int(row[6]))
    # values.append(values1)
    # values.append(values2)
    return values
lst = actAndSat(data1)
df = pd.DataFrame(lst,columns=['test preparation course','ACT composite score','SAT total score'])
box_plot = sns.boxplot(x="test preparation course", y="ACT composite score", data=df)

ax = box_plot.axes
lines = ax.get_lines()
categories = ax.get_xticks()
def addValueInBoxPlot(data):
    for cat in categories:
    # every 4th line at the interval of 6 is median line
    # 0 -> p25 1 -> p75 2 -> lower whisker 3 -> upper whisker 4 -> p50 5 -> upper extreme value
        median = round(lines[4+cat*6].get_ydata()[0],1)
        p25 = round(lines[0 + cat * 6].get_ydata()[0], 1)
        p75 = round(lines[1 + cat * 6].get_ydata()[0], 1)
    #exvalue = round(lines[5 + cat * 6].get_ydata()[0], 1)
        lwh = round(lines[2 + cat * 6].get_ydata()[0], 1)
        uwh = round(lines[3 + cat * 6].get_ydata()[0], 1)

        ax.text(
            cat,
            median,
            f'{median}',
            ha='center',
            va='center',
            fontweight='bold',
            size=10,
            color='white',
            bbox=dict(facecolor='#445A64')
        )
        ax.text(
            cat,
            p25,
            f'{p25}',
            ha='center',
            va='center',
            fontweight='bold',
            size=10,
            color='white',
            bbox=dict(facecolor='#445A64')
        )
    # ax.text(
    #     cat,
    #     exvalue,
    #     f'{exvalue}',
    #     ha='center',
    #     va='center',
    #     fontweight='bold',
    #     size=10,
    #     color='white',
    #     bbox=dict(facecolor='#445A64')
    # )
        ax.text(
            cat,
            lwh,
            f'{lwh}',
            ha='center',
            va='center',
            fontweight='bold',
            size=10,
            color='white',
            bbox=dict(facecolor='#445A64')
        )
        ax.text(
            cat,
            uwh,
            f'{uwh}',
            ha='center',
            va='center',
            fontweight='bold',
            size=10,
            color='white',
            bbox=dict(facecolor='#445A64')
        )
        ax.text(
            cat,
            p75,
            f'{p75}',
            ha='center',
            va='center',
            fontweight='bold',
            size=10,
            color='white',
            bbox=dict(facecolor='#445A64')
        )
    box_plot.figure.tight_layout()
    return box_plot
addValueInBoxPlot(df)
plt.savefig('fig2.png')
#df = pd.DataFrame()
# lst_none = actAndSat('none',data1)
# lst_completed = actAndSat('completed',data1)
# lst_all_act = lst_none[0],lst_completed[0]
# box_plot = plt.boxplot(lst_all_act,patch_artist=True,labels=['None','Completed'])
# plt.xlabel('Test preparation course')
# plt.ylabel('ACT composite score')
plt.show()
#plt.savefig('fig2.png')
# lst_all_sat = lst_none[1],lst_completed[1]
# plt.boxplot(lst_all_sat,patch_artist=True,labels=['None','Completed'])
# plt.xlabel('Test preparation course')
# plt.ylabel('SAT total score')
# plt.show()
#plt.savefig('fig3.png')
lst2 = actAndSat(data1)
df2 = pd.DataFrame(lst,columns=['test preparation course','ACT composite score','SAT total score'])
box_plot2 = sns.boxplot(x="test preparation course", y="SAT total score", data=df2)
ax = box_plot2.axes
lines = ax.get_lines()
categories = ax.get_xticks()

addValueInBoxPlot(df2)
plt.savefig('fig3.png')
plt.show()