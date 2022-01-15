import pandas as pd
import matplotlib.pyplot as plt
import datetime
df = pd.read_excel(r'/home/aman/Desktop/weather_data_kolkata_2015_2020.xlsx')
print(df)

x= list(df['TEMPERATURE'])
y= list(df['HUMIDITY'])
z = list(df['DATETIME'])
n=len(z)

# for i in range(n):
#     z[i]= datetime.datetime(int(z[i][:4]), int(z[i][5:7]), int(z[i][8:10]), 0, 0).timestamp()

plt.figure(figsize=(10,10))
plt.style.use("seaborn")
plt.scatter(x,y,marker="*", s = 100)
plt.title("Temperature vs Humidity")
plt.show()

