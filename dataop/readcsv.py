# -*- coding: UTF-8 -*-
import pandas
import numpy as np
import matplotlib.pyplot as plt


def rdcsv(filename, skipRow=34, nRows=1000):
    d = pandas.read_csv(filename, skiprows=skipRow,nrows=nRows, header=None)
    d.columns = ['Wavelength', 'Loss']
    return d

def getMeanDF(dataFrame, div_size, fromwl, towl):
    wl_list = []
    loss_list = []
    w = dataFrame['Wavelength']
    l = dataFrame['Loss']
    data_num = len(w)
    # print(data_num)
    # print('from {} to {}'.format(w[0], w[999]))
    if div_size > 1:    #<=1就不光滑化处理，否则就取相近的div_size个数进行平均值计算
        for i in range(0, data_num):
            if i+div_size <= data_num:
                ww = w[i:i+div_size].mean()
                ll = l[i:i+div_size].mean()
                wl_list.append(ww)
                loss_list.append(ll)
        dataFrame.drop(dataFrame.index,inplace=True)
        dataFrame['Wavelength'] = wl_list
        dataFrame['Loss'] = loss_list
    df = dataFrame[(dataFrame['Wavelength'] > fromwl) & (dataFrame['Wavelength'] < towl)]
    # print(df)
    return df

def cutDataAndGetMin1(dataFrame, fromIndex, toIndex):
    cutData = dataFrame[fromIndex : toIndex]
    selData = cutData[cutData.Loss == cutData['Loss'].min()]
    wl = selData['Wavelength'].values[0]
    loss = selData['Loss'].values[0]
    return wl, loss
    
def getMinWl(dataFrame):
    selData = dataFrame[dataFrame.Loss == dataFrame['Loss'].min()]
    wl = selData['Wavelength'].values[0]
    loss = selData['Loss'].values[0]
    return wl, loss

# 曲线拟合后，取最小值  
def getMinWlByPolyFit(dataFrame, db):
    w = dataFrame['Wavelength']
    l = dataFrame['Loss']
    size = w.values.size
    wmin = round(w.values[0], 2)
    wmax = round(w.values[size - 1], 2)
    x = np.arange(wmin, wmax, 0.01)
    # print('min:{}, max:{}. '.format(w.values[0], w.values[size - 1]))
    fitFun = np.polyfit(w, l, 4)
    p = np.poly1d(fitFun)
    y = p(x)
    
    # plt.plot(w, l, linewidth=1, color='red')
#     plt.plot(x, y, linewidth=1, color='blue')
#     plt.show()
    
    d = {}
    d['Wavelength'] = x
    d['Loss'] = y
    df = pandas.DataFrame(d)
    selData = df[df.Loss == df['Loss'].min()]
    lm = selData['Loss'].values[0]
    wm = selData['Wavelength'].values[0]
    lminAdd = lm +db
    x1 = wm
    ll = p(x1)
    while ll < lminAdd:
        x1 += 0.01
        ll = p(x1)
    
    x2 = wm
    ll = p(x2)
    while ll < lminAdd:
        x2 -= 0.01
        ll = p(x2)
    minwl = (x1 + x2) / 2
    # q = np.polyder(p)#求导
    # print(q)
    return minwl, lm
    

def main():
    path = '/Users/haiou/Desktop/exp_result/4-Octadecane-3-1120/data/W20191120_174520.CSV'
    d = rdcsv(path)
    df = getMeanDF(d, 1, 1507, 1522)
    d = getMinWlByPolyFit(df, 3)
    print(d)
    # # print(result[0], result[1])
    # w = d['Wavelength']
    # l = d['Loss']
    # plt.plot(w, l, linewidth=1, color='red')
    # plt.show()

if __name__ == '__main__':
    main()

# cutd = d[1:10]
# print(d)
# seld = cutd[cutd.Loss == cutd['Loss'].min()]
# print(seld['Wavelength'].values[0])
# print(seld['Loss'].values[0])
# print(d.shape[0])
# print(d.shape[1])