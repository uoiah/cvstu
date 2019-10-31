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

def main():
    path = '../exp_result/s46-10-1/W20191026_104624.CSV'
    d = rdcsv(path)
    df = getMeanDF(d, 24, 1500, 1600)
    result = getMinWl(df)
    print(result[0], result[1])
    w = df['Wavelength']
    l = df['Loss']
    plt.plot(w, l, linewidth=1, color='red')
    plt.show()

if __name__ == '__main__':
    main()

# cutd = d[1:10]
# print(d)
# seld = cutd[cutd.Loss == cutd['Loss'].min()]
# print(seld['Wavelength'].values[0])
# print(seld['Loss'].values[0])
# print(d.shape[0])
# print(d.shape[1])