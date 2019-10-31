import matplotlib
# matplotlib.use('agg')
import pandas
import numpy as np
import matplotlib.pyplot as plt

def getMeanDF(dataFrame, div_size):
    wl_list = []
    t_list = []
    w = dataFrame['Wavelength']
    t = dataFrame['Temperature']
    data_num = len(w)
    for i in range(0, data_num):
        if i+div_size <= data_num:
            ww = w[i:i+div_size].mean()
            tt = t[i:i+div_size].mean()
            wl_list.append(ww)
            t_list.append(tt)
    dataFrame.drop(dataFrame.index,inplace=True)
    dataFrame['Wavelength'] = wl_list
    dataFrame['Temperature'] = t_list
    return dataFrame

def drawPlot(heatDir, coldDir):
      
    df = pandas.read_excel(heatDir + "result.xlsx")
    
    # df = getMeanDF(df, 8)
    wheat = df['Wavelength']
    theat = df['Temperature']

    df = pandas.read_excel(coldDir + "result.xlsx")
    # df = getMeanDF(df, 24)
    wcold = df['Wavelength']
    tcold = df['Temperature']
    # y = np.array([funtest(x) for x in t])

    # x = np.linspace(-1, 2, 50)
    # y1 = x ** 2
    # y2 = np.sin(x)

    fig = plt.figure()
    plt.plot(theat, wheat, color='red', label='Heating cycle', linewidth=1)
    # plt.plot(x, y2, color='red', linestyle='--', linewidth=1, label='sin')
    plt.xlabel('Temperature(°C)')
    plt.ylabel('Wavelength(nm)')

    plt.plot(tcold, wcold, color='blue',label='Colding cycle', linewidth=1)
    # plt.plot(x, y2, color='red', linestyle='--', linewidth=1, label='sin')
    plt.xlabel('Temperature(°C)')
    plt.ylabel('Wavelength(nm)')
    # x_ticks = np.linspace(-1,2,10)
    # y_ticks = np.linspace(-1,5,10)
    # plt.xticks(x_ticks)
    # plt.yticks(y_ticks)

    plt.grid()
    plt.legend(loc='center right')
    # fig.savefig("curve_tmp.png")
    plt.show()
    
def main():
    
    drawPlot("../exp_result/S46-10-1/heat/", "../exp_result/S46-10-1/cold/")
    
if __name__ == '__main__':
    main()