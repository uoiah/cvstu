import numpy as np
import matplotlib.pyplot as plt
import pandas


path = '/Users/haiou/Desktop/exp_result/e-Octadecane-14-1208/data/W20191208_103244.CSV'
d = pandas.read_csv(path, skiprows=34,nrows=2001, header=None)
d.columns = ['Wavelength', 'Loss']
# print(d)

w = d['Wavelength']
l = d['Loss']
size = w.values.size
# wmin = round(w.values[0], 2)
#     wmax = round(w.values[size - 1], 2)
x = np.arange(1550, 1590, 0.01)
# print('min:{}, max:{}. '.format(w.values[0], w.values[size - 1]))
fitFun = np.polyfit(w, l, 4)
p = np.poly1d(fitFun)
y = p(x)
# d = {}
# d['Wavelength'] = x
# d['Loss'] = y

plt.plot(w, l, linewidth=1, color='r')
plt.plot(x, y, color='b',linewidth=1,linestyle=':')
plt.show()