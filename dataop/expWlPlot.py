import matplotlib
# matplotlib.use('agg')
import pandas
import numpy as np
import matplotlib.pyplot as plt

df = pandas.read_excel("/Users/haiou/Desktop/exp_result/5-Octadecane-3-1121/result.xlsx")
    
size_heat = df.shape[0]
time_heat = np.arange(0, size_heat, 1)
wheat = df['Wavelength']
theat = df['Temperature']

plt.figure(figsize=(12, 6))

ax1 = plt.subplot(111)
plt.plot(time_heat, wheat, color='red', label='WaveLength', linewidth=1)
plt.xlabel('Time(minute)')
plt.ylabel('Wavelength(nm)')
plt.grid()

ax3 = ax1.twinx()
plt.plot(time_heat, theat, color='blue', label='Temeprature', linewidth=1)
plt.xlabel('Time(minute)')
plt.ylabel('Temperature(°C)')
# plt.legend(loc='center right')
# fig.savefig("curve_tmp.png")
plt.show()