import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci

uplimitp = 7.1
uplimit = 20
p = 0-uplimitp
increment = 1/30
x = np.linspace(0-uplimit, uplimit, 100)
plt.figure(figsize=(5, 5), layout='constrained')


while(p < uplimitp):
    a = sci.gamma(p) * sci.digamma(p)
    b = sci.gamma(p) - (a * p)
    plt.plot(x, a*x + b, color="black", linewidth="0.2")
    p += increment / (0.5 + abs(1/(1 + a**2) * (a + (sci.gamma(p) * sci.polygamma(1, p)))))
    
plt.axis("equal")
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.show()

