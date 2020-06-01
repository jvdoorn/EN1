import numpy as np
from numpy.ma import sqrt

series1 = np.genfromtxt('data/resultaten b2 1.csv', delimiter=',')
series2 = np.genfromtxt('data/resultaten b2 2.csv', delimiter=',')

series1mean = series1.mean()
series2mean = series2.mean()

series1f = sqrt(((series1 - series1mean) ** 2).sum())
series2f = sqrt(((series2 - series2mean) ** 2).sum())

R = series1mean
Rf = series1f
series1T = 30.84 + (2.232 * R) + (2.43 * 10 ** -3 * R ** 2) - (5.33 * 10 ** -6 * R ** 3)
series1Tf = (Rf / R) * 2.232 + 2 * (Rf / R) * 2.43 + 3 * (Rf / R) * 5.33

R = series2mean
Rf = series2f
series2T = 30.84 + (2.232 * R) + (2.43 * 10 ** -3 * R ** 2) - (5.33 * 10 ** -6 * R ** 3)
series2Tf = (Rf / R) * 2.232 + 2 * (Rf / R) * 2.43 + 3 * (Rf / R) * 5.33
