# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#求函数f的导数
def numeric_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)
    
#一维数组的梯度
def _numerical_gradient_1d(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 还原值
        
    return grad

#二维数组的梯度，一维也可
def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_1d(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_1d(f, x)
        
        return grad
               
#梯度下降  
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numeric_gradient(f, x)
        x -= lr * grad
    return x


#以下为测试代码
def ng(f, x):
    delta = 1e-4
    x1 = x - delta / 2
    x2 = x + delta / 2
    dx = x2 - x1
    y1 = f(x1)
    y2 = f(x2)
    dy = y2 - y1
    return dy / dx
    

def fun1(x):
    return x ** 2
    
def fun2(x, x1):
    slop1 = ng(fun1, x1)
    return slop1 * (x - x1) + fun1(x1)


def drawPlot():
    x = np.arange(-20, 20, 1)
    y1 = fun1(x)
    y2 = fun2(x, 5)
    # plt.scatter(x, y)
    plt.plot(x, y1)
    plt.plot(x, y2)

    plt.show()
    
    
if __name__ == '__main__':
    drawPlot()
    
