from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
df = pd.read_excel(r'/home/aman/Desktop/weather_data_kolkata_2015_2020.xlsx')
print(df)



x = np.linspace(-4*np.pi,4*np.pi,50)

y = np.linspace(-4*np.pi,4*np.pi,50)

z = x**2 + y**2

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.plot(x,y,z)

plt.show()