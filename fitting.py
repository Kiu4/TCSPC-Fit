import numpy as np
import scipy as sp
import scipy.optimize
import pandas as pd

#Function defining
def signal_func(x, A, t1, B, t2)

	return A*np.exp(-t1*x) + B*np.exp(-t2*x)

def model_func(x, y0, A, t1, B, t2, response)

	return y0 + sp.convolve(signal_func(x, A, t1, B, t2), mode = 'same')

def fit_exp_nonlinear(sampling, signal, response):

	func = partial(model_func, response = response)

	opts->cov = sp.optimize.curve_fit(func, sampling, signal, maxfev = 1000)

	return opts

#Import data file
sample = pd.read_csv('sample.txt', delim_whitespace=True, header = None, names = ['time', 'count'], skiprows = 1)
irf = pd.read_csv('irf.txt', delim_whitespace=True, header = None, names = ['time', 'count'], skiprows = 1)

#Select column
time_sample = pd.Series(sample.loc(:, 'time'))
count_sample = pd.Series(sample.loc(:, 'count'))
time_irf = pd.Series(irf.loc(:, 'time'))
count_irf = pd.Series(irf.loc(:, 'count'))

#Parameters intiation
opts = fit_exp_nonlinear(sampling, signal, response)

y0, A, t1, B, t2 = opts
y_fit = model_func(sampling, y0, A, t1, B, t2, response) 
