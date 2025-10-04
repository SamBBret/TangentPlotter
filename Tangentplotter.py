import numpy as np
import matplotlib.pyplot as plt

uplimit = 10*np.pi
p = 0 - uplimit
increment = 1/30
x = np.linspace( 0 - uplimit, uplimit, 100)
plt.figure(figsize=(5, 5), layout='constrained')


while(p < uplimit):
    a = 1 - ((p**2) / 2) + ((p**4) / 24)
    b = (2 * (p**3) / 6) - (4 * (p**5) / 120)
    plt.plot(x, (a*x) + b, color="black", linewidth="0.2")
    p += increment / (0.1 + abs(1/(1 + a**2) * (0 - p + ((p**3)/6))))

plt.axis("equal")
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.show()
