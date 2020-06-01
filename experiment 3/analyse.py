import matplotlib.pyplot as plt
import numpy as np

series = np.genfromtxt('data/c-meeting-rustig-koelen.csv', delimiter=',')

M = lambda N: 1000 * N
T = lambda R: 30.84 + (2.232 * R) + (2.43 * 10 ** -3 * R ** 2) - (5.33 * 10 ** -6 * R ** 3)

temp_series = T(M(series[:, 2]))
resistance_series = M(series[:, 1])
resistance_series_d = np.gradient(resistance_series)

print(series[:, 2][resistance_series_d.argmin()])
print(temp_series[resistance_series_d.argmin()])

# print(resistance_series_d.min())
# print(resistance_series_d.argmin())


# plt.plot(temp_series, resistance_series_d)
# plt.xlabel('Temperature (K)')
# plt.ylabel('Resistance delta (\u03A9)')
# plt.savefig("1.png")
#
# plt.plot(temp_series, resistance_series)
# plt.xlabel('Temperature (K)')
# plt.ylabel('Resistance (\u03A9)')
# plt.savefig("2.png")