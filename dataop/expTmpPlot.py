import matplotlib
# matplotlib.use('agg')
import pandas
import numpy as np
import matplotlib.pyplot as plt

def drawTmpPlot(tmpFile):
      
    df = pandas.read_excel('../exp_result/' + tmpFile)
    i = df['id']
    t = df['temp']
    # y = np.array([funtest(x) for x in t])

    # x = np.linspace(-1, 2, 50)
    # y1 = x ** 2
    # y2 = np.sin(x)

    fig = plt.figure()
    plt.plot(i, t, color='red', label='Heating cycle', linewidth=1)
    # plt.plot(x, y2, color='red', linestyle='--', linewidth=1, label='sin')
    plt.ylabel('Temperature(°C)')
    plt.xlabel('Time(M)')

    plt.grid()
    plt.legend(loc='upper right')
    # fig.savefig("curve_tmp.png")
    plt.show()
    
def main():
    drawTmpPlot('s46-10-tmp-1.xlsx')
    
if __name__ == '__main__':
    main()