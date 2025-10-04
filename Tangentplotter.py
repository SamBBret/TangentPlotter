import numpy as np
import matplotlib.pyplot as plt

uplimit = 5*np.pi
p = 0-uplimit
increment = 1/30
x = np.linspace(0-uplimit, uplimit, 100)
plt.figure(figsize=(5, 5), layout='constrained')


while(p < uplimit):
    a = np.cos(p)
    b = np.sin(p) - np.cos(p) * p
    plt.plot(x, a*x + b, color="black", linewidth="0.2")
    p += increment / (0.1 + abs(1/(1 + a**2) * (-np.sin(p))))

p = 0-uplimit

while(p < uplimit):
    a = 1 - ((p**2) / 2) + ((p**4) / 24) - ((p**6) / 720) + ((p**8) / 40320)
    b = (2 * (p**3) / 6) - (4 * (p**5) / 120) + (6 * (p**7) / 5040) - (8 * (p**9) / 362880)
    plt.plot(x, (a*x) + b, color="red", linewidth="0.2")
    p += increment / (0.1 + abs(1/(1 + a**2) * (0 - p + ((p**3)/6) - ((p**5) / 120) + ((p**7) / 5040))))

plt.axis("equal")
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.show()

