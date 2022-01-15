import pandas as pd
import matplotlib.pyplot as plt
import datetime
df = pd.read_excel(r'/home/aman/Desktop/weather_data_kolkata_2015_2020.xlsx')
print(df)

x= list(df['TEMPERATURE'])
y= list(df['HUMIDITY'])
z = list(df['DATETIME'])

plt.figure(figsize=(10,10))
plt.style.use("seaborn")
plt.scatter(x,z,marker="*", s = 100)
plt.title("Temperature vs Year")
plt.show()