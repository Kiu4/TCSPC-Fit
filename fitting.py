import numpy as np
import scipy as sp
import scipy.optimize
import pandas as pd
from functools import partial

#Function defining
def signal_func(x, A, t1, B, t2):

	return A*np.exp(-t1*x) + B*np.exp(-t2*x)

def model_func(x, y0, A, t1, B, t2, response):

	return y0 + sp.convolve(signal_func(x, A, t1, B, t2), response, mode = 'same')

def fit_exp_nonlinear(sampling, signal, response, initiation):

	func = partial(model_func, response = response)

	opts, cov = sp.optimize.curve_fit(func, sampling, signal, p0 = initiation, maxfev = 1000)

	return opts

#Import data file
sample = pd.read_csv('sample.txt', delim_whitespace=True, header = None, names = ['time', 'count'], skiprows = 1)
irf = pd.read_csv('irf.txt', delim_whitespace=True, header = None, names = ['time', 'count'], skiprows = 1)

time = pd.Series(sample['time'])
count_sample = pd.Series(sample['count'])
count_irf = pd.Series(irf['count'])

initiation = np.array([0, 0.5, 100, 0.5, 1000])


#Intiation Reconvolutin
opts = fit_exp_nonlinear(time, count_sample, count_irf, initiation)

y0, A, t1, B, t2 = opts
y_fit = model_func(time, y0, A, t1, B, t2, count_irf) 

result = pd.DataFrame(sample['time'])

result = pd.concat([result, pd.DataFrame(y_fit)], axis = 1)

print(result)