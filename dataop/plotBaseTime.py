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

    fig = plt.figure(figsize=(8, 6))
    
    ax1 = plt.subplot(321)
    plt.plot(time_heat, wheat, color='red', label='WaveLength', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Wavelength(nm)')
    
    ax3 = plt.subplot(323)
    plt.plot(time_heat, theat, color='blue', label='Temeprature', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Temperature(°C)')
    
    ax5 = plt.subplot(325)
    plt.plot(time_heat, lheat, color='green', label='Loss', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Loss(db)')
    
    ax2 = plt.subplot(322)
    plt.plot(time_cold, wcold, color='red',label='WaveLength', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Wavelength(nm)')
    
    ax4 = plt.subplot(324)
    plt.plot(time_cold, tcold, color='blue', label='Temeprature', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Temperature(°C)')
    
    ax6 = plt.subplot(326)
    plt.plot(time_cold, lcold, color='green', label='Loss', linewidth=1)
    plt.xlabel('Time(minute)')
    plt.ylabel('Temperature(°C)')
    
    # plt.plot(x, y2, color='red', linestyle='--', linewidth=1, label='sin')
    # x_ticks = np.linspace(-1,2,10)
    # y_ticks = np.linspace(-1,5,10)
    # plt.xticks(x_ticks)
    # plt.yticks(y_ticks)

    plt.grid()
    # plt.legend(loc='center right')
    # fig.savefig("curve_tmp.png")
    plt.show()
    
def main():
    
    drawPlot("../../exp_result/3-Octadecane-10-1117/")
    
if __name__ == '__main__':
    main()