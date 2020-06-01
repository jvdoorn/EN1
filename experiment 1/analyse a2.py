from math import sqrt

V = 1.01442  # Volts
I = 9.3297 * 10 ** -3  # Amps

Vf = 0.00015 * V + 0.00003 * 2  # Volts
If = 0.00055 * I + 0.00005 * 2 * 10 ** -3  # Amps

R = V / I  # Ohms
Rf = sqrt((Vf / V) ** 2 + (If / I) ** 2)  # Ohms

T = 30.84 + (2.232 * R) + (2.43 * 10 ** -3 * R ** 2) - (5.33 * 10 ** -6 * R ** 3)  # Kelvin
Tf = (Rf / R) * 2.232 + 2 * (Rf / R) * 2.43 + 3 * (Rf / R) * 5.33  # Kelvin
