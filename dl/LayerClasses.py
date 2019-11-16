import numpy as np
from func import *
class Affine:
	def __init__(self, W, b):
		self.W = W
		self.b = b
		self.x = None
		self.dW = None
		self.db = None
		
	def forward(self, x):
		self.x = x
		r = np.dot(x, self.W) + self.b
		return r
		
	def backward(self, dr):
		dx = np.dot(dr, self.W.T)
		dW = np.dot(self.x.T, dr)
		db = np.sum(dr, axis=0)
		return dx
		
class SoftmaxWithLoss:
	def __init__(self):
		self.loss = None
		self.y = None
		self.t = None
		
	def forward(self, x, t):
		self.t = t
		self.y = softmax(x)
		self.loss = cross_entrop_error(self.y, self.t)
		return self.loss
		
	def backward(self, dr=1):
		batch_size = self.t.shape[0]
		dx = (self.y - self.t) / batch_size
		return dx