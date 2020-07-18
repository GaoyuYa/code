# coding:utf-8
from matplotlib import pyplot as plt
from datetime import datetime

data = ['64', '71', '64', '59', '69', '62', '57', '87', '89','64', '71', '64', '59', '69', '62', '57', '87', '89']
data = ['64', '71', '64', '59', '69', '62', '57', '87', '89','64', '71', '64', '59', '69', '62', '57', '87', '89']
print dat
data = ['64', '71', '64', '59', '69', '62', '57', '87', '89','64', '71', '64', '59', '69', '62', '57', '87', '89']
int_data = []
date=[]
for row in data:
    #current_date=datetime.strptime(row[0],"%Y-%m-%d")
    high = int(row)
    int_data.append(high)
    #date.append(current_date)

fig = plt.figure(dpi=64, figsize=(20, 12))
plt.plot(int_data, c='blue')
plt.title(u"test data", fontsize=16)
plt.xlabel(u"time", fontsize=16)
plt.ylabel(u"CPU%", fontsize=20)
plt.show()
data = ['64', '71', '64', '59', '69', '62', '57', '87', '89','64', '71', '64', '59', '69', '62', '57', '87', '89']
data = ['64', '71', '64', '59', '69', '62', '57', '87', '89','64', '71', '64', '59', '69', '62', '57', '87', '89']
