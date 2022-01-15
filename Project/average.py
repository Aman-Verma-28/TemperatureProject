from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
df = pd.read_excel(r'/home/aman/Desktop/weather_data_kolkata_2015_2020.xlsx')
# print(df)

x= list(df['TEMPERATURE'])
y= list(df['HUMIDITY'])
z = list(df['DATETIME'])
dateTime=pd.to_datetime(df['DATETIME']).dt.date
print(type(z[0]))
d={}
print(dateTime)
for i in range(len(z)):
    if z[i] in d:
        d[z[i]][0]+=x[i]
        d[z[i]][1]+=y[i]
        d[z[i]][2]+=1
    else:
        d[z[i]]=[x[i],y[i],1]

# print(d)

for i in d:
    print("Average temperature for",i,":", d[i][0]/d[i][2])
    print("Average humidity for",i,":", d[i][1]/d[i][2])