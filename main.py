import matplotlib.pyplot as plt
import numpy as np
# constants for CO2
a = 3.59
b = 0.0427
R = 0.0821

T = a/(R*b)
T_dash = 398
V = np.linspace(1, 30, 100)
print(T)
P1 = R*T/(V-b) - a/V**2
P2 = (R*T)/V
P3 = R*T_dash/(V-b) - a/V**2
plt.figure()
plt.plot(V, P1, label=f"T = {T}K")
plt.plot(V, P2, label= f"T = {T}K, ideal gas")
plt.plot(V, P3, label = f"T= {T_dash}K")
plt.xlabel("Volume")
plt.ylabel("Pressue")
plt.title("Van der Waals equation graph for CO2")
plt.legend()
plt.show()