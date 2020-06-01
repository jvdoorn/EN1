import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

Vex = 5  # Volt
Rs = 4.12 * 10 ** 3  # Ohm

series = np.genfromtxt('data/meting 1.csv', delimiter=',')

R = lambda V: Rs * ((1 - (V / Vex)) / (1 + (V / Vex)))
B = lambda R: (500 / ((3.69 - 4.12) * 10 ** 3)) * (R - Rs)

time_series = series[:, 0][int(4.4125 * 20000): int(4.42 * 20000)]
voltage_series = series[:, 1][int(4.4125 * 20000): int(4.42 * 20000)]

resistance_series = R(voltage_series)
magnetic_series = B(resistance_series)
magnetic_log_series = np.log(magnetic_series)

slope, intercept, r_value, p_value, std_err = stats.linregress(time_series, magnetic_log_series)

# plt.plot(time_series, magnetic_series)
# plt.xlabel('Time (s)')
# plt.ylabel('Ln of the Magnetic Field Strength (G)')
# plt.savefig('figure6.png')
# plt.show()
