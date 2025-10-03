import numpy as np
import matplotlib.pyplot as plt

uplimit = 2*np.pi
p = 0-uplimit
increment = 1/7
x = np.linspace(0-uplimit, uplimit, 100)
plt.figure(figsize=(5, 2.7), layout='constrained')


while(p < uplimit):
    a = np.cos(p)
    b = np.sin(p) - np.cos(p) * p
    plt.plot(x, a*x + b, color="black", linewidth="0.5")
    p += increment / (0.3 + np.abs(0 - np.sin(p)))

p = 0-uplimit
increment= 1/10



plt.show()

