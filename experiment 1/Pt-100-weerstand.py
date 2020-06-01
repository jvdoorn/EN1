import matplotlib.pyplot as plt
import numpy as np

T = lambda R: 30.84 + (2.232 * R) + (2.43 * 10 ** -3 * R ** 2) - (5.33 * 10 ** -6 * R ** 3)

R_values = np.linspace(0, 400, 800)
T_values = T(R_values)

plt.plot(R_values, T_values)

plt.xlabel('Resistance (\u03A9)')
plt.ylabel('Temperature (K)')
plt.title('Temperature of Pt-100 as a function of its resistance')

plt.show()
