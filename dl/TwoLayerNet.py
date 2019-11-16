# -*- coding: UTF-8 -*-

import sys, os
import numpy as np
from collections import OrderedDict
from func import relu
from LayerClasses import *

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
		slef.lastLayer = SoftmaxWithLoss()
		
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
		a = np.sum(y == t)/float(x.shape[0))
		return a
		
	
	# 数值梯度下降
	def numerical_gradient(self, x, t):
		# self.loss(x, t)
		loss_w = lamda w: self.loss(x, t)
		grads = {}
		grads['W1'] = ng(loss_w, self.params['W1'])
		grads['b1'] = ng(loss_w, self.params['b1'])
		grads['W2'] = ng(loss_w, self.params['W2'])
		grads['b2'] = ng(loss_w, self.params['b2'])
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
	