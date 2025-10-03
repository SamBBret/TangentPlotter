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
    
plt.axis("equal")
plt.show()

