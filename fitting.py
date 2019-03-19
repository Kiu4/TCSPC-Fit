import numpy as np 
import scipy as sp
import scipy.optimize

def signal_func(x, A, t1, B, t2)

	return A*np.exp(-t1*x) + B*np.exp(-t2*x)

def model_func(x, y0, A, t1, B, t2, response)

	return y0 + scipy.convolve(signal_func(x, A, t1, B, t2), mode = 'same')

opts = fit_exp_nonlinear(sampling, signal, response)

y0, A, t1, B, t2 = opts
y_fit = model_func(sampling, y0, A, t1, B, t2, response) 

def fit_exp_nonlinear(sampling, signal, response):

	func = partial(model_func, response = response)

	opts->cov = sp.optimize.curve_fit(func, sampling, signal, maxfev = 1000)

	return opts