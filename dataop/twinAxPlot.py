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

def drawPlot(dataDir):
      
    df = pandas.read_excel(dataDir + "heat.xlsx")
    
    
    # df = getMeanDF(df, 8)
    size_heat = df.shape[0]
    time_heat = np.arange(0, size_heat, 1)
    wheat = df['Wavelength']
    theat = df['Temperature']
    lheat = df['Loss']

    df = pandas.read_excel(dataDir + "cold.xlsx")
    # df = getMeanDF(df, 8)
    size_cold = df.shape[0]
    time_cold = np.arange(0, size_cold, 1)
    wcold = df['Wavelength']
    tcold = df['Temperature']
    lcold = df['Loss']
    # y = np.array([funtest(x) for x in t])

    # x = np.linspace(-1, 2, 50)
    # y1 = x ** 2
    # y2 = np.sin(x)

    plt.figure(figsize=(12, 6))
    
    ax1 = plt.subplot(121)
    plt.plot(time_heat, wheat, color='red', label='WaveLength', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Wavelength(nm)')
    plt.grid()
    
    ax3 = ax1.twinx()
    plt.plot(time_heat, theat, color='blue', label='Temeprature', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Temperature(°C)')
    # plt.grid()

    
    ax2 = plt.subplot(122)
    plt.plot(time_cold, wcold, color='red',label='WaveLength', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Wavelength(nm)')
    plt.grid()
    
    ax4 = ax2.twinx()
    plt.plot(time_cold, tcold, color='blue', label='Temeprature', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Temperature(°C)')
    # plt.grid()

    
    # plt.plot(x, y2, color='red', linestyle='--', linewidth=1, label='sin')
    # x_ticks = np.linspace(-1,2,10)
    # y_ticks = np.linspace(-1,5,10)
    # plt.xticks(x_ticks)
    # plt.yticks(y_ticks)

    
    fig = plt.gcf()
    fig.tight_layout()
    # plt.legend(loc='center right')
    # fig.savefig("curve_tmp.png")
    plt.show()
    
def main():
    
    drawPlot("../../exp_result/1-Octadecane-10-1116/")
    
if __name__ == '__main__':
    main()