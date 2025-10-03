import numpy as np
import matplotlib.pyplot as plt

p = 0.0
uplimit = 11*np.pi
increment = 1/10
x = np.linspace(0, uplimit, 100)
plt.figure(figsize=(5, 2.7), layout='constrained')


while(p < uplimit):
    a = np.cos(p)
    b = np.sin(p) - np.cos(p) * p
    plt.plot(x, a*x + b, color="black", linewidth="0.2")
    p += increment

plt.show()
