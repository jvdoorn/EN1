import matplotlib.pyplot as plt
import numpy as np

T = lambda R: 30.84 + (2.232 * R) + (2.43 * 10 ** -3 * R ** 2) - (5.33 * 10 ** -6 * R ** 3)

R_values = np.linspace(0, 400, 1600)
T_values = T(R_values)

plt.plot(T_values, R_values)

plt.xlabel('Temperature (K)')
plt.ylabel('Resistance (\u03A9)')
plt.title('Resistance of Pt-100 as a function of its temperature')

plt.show()
