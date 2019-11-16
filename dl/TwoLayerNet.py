# -*- coding: UTF-8 -*-

import sys, os
import numpy as np
from collections import OrderedDict
from LayerClasses import *
from sgd import numerical_gradient

class TwoLayerNet:
	def __init__(self, inputSize, hiddenSize, outputSize, weightInit=0.01):
		self.params = {}
		self.params['W1'] = weightInit * np.random.randn(inputSize, hiddenSize)
		self.params['b1'] = np.zeros(hiddenSize)
		self.params['W2'] = weightInit * np.random.randn(hiddenSize, outputSize)
		self.params['b2'] = np.zeros(outputSize)
		
		self.layers = OrderedDict()
		self.layers['affine1'] = Affine(self.params['W1'], self.params['b1'])
		self.layers['relu'] = Relu()
		self.layers['affine2'] = Affine(self.params['W2'], self.params['b2'])
		self.lastLayer = SoftmaxWithLoss()
		
	def predict(self, x):
		for layer in self.layers.values():
			x = layer.forward(x)
			
		return x
		
	def loss(self, x, t):
		y = self.predict(x)
		y = self.lastLayer.forward(y, t)
		
		return y
		
	def accuracy(self, x, t):
		y = self.predict(x)
		y = np.argmax(y, axis=1)
		if t.ndim != 1:
			t = np.argmax(t, axis=1)
		a = np.sum(y == t)/float(x.shape[0])
		return a
		
	
	# 数值梯度
	def num_gradient(self, x, t):
		# self.loss(x, t)
		loss_w = lambda w : self.loss(x, t)
		grads = {}
		grads['W1'] = numerical_gradient(loss_w, self.params['W1'])
		grads['b1'] = numerical_gradient(loss_w, self.params['b1'])
		grads['W2'] = numerical_gradient(loss_w, self.params['W2'])
		grads['b2'] = numerical_gradient(loss_w, self.params['b2'])
		return grads
		
	# 反向误差传播
	def gradient(self, x, t):
		self.loss(x, t)
		dout = 1
		dout = self.lastLayer.backward(dout)
		layers = list(self.layers.values())
		layers.reverse()
		for layer in layers:
			dout = layer.backward(dout)
			
		grads = {}
		grads['W1'] = self.layers['affine1'].dW
		grads['b1'] = self.layers['affine1'].db
		grads['W2'] = self.layers['affine2'].dW
		grads['b2'] = self.layers['affine2'].db
		
		return grads
        
def test():
    net = TwoLayerNet(3, 5, 2)
    x = np.array([[123,231,11],[45, 67, 156]])
    t = np.array([[1,1],[2,2]])
    # y = net.predict(x)
    l = net.loss(x, t)
    print(l)
    
if __name__ == '__main__':
    test()
	