import numpy as np

def relu(x):
	return np.maximum(0, x)

def softmax(x):
	c = np.max(x)
	exp_a = np.exp(x - c)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
    # print(y.shape)
	return y


def cross_entrop_error(y, t):
	delta = 1e-7
	return -np.sum(t * np.log(y + delta))

	