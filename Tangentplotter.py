import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci

functionlimit = 5*np.pi
uplimit = 5*np.pi
sidelimit = 6*np.pi
p = 0-functionlimit
increment = 1/30
plt.figure(figsize=(5, 5), layout='constrained')

counter = 0

while(p < functionlimit):
    counter += 1
    xpoint = []
    ypoint = []
    a = sci.digamma(p) * sci.gamma(p)
    b = sci.gamma(p) - a * p
    c = a * (-sidelimit) + b
    if abs(c) <= uplimit:
        xpoint.append(-sidelimit)
        ypoint.append(c)
    c = a * sidelimit + b
    if abs(c) <= uplimit:
        xpoint.append(sidelimit)
        ypoint.append(c)
    c = (-uplimit - b) / a
    if abs(c) < sidelimit:
        xpoint.append(c)
        ypoint.append(-uplimit)
    c = (uplimit - b) / a
    if abs(c) < sidelimit:
        xpoint.append(c)
        ypoint.append(uplimit)

    plt.plot(xpoint, ypoint, color="black", linewidth="0.2")
    p += increment / (0.5 + abs(1/(1 + a**2) * (a + (sci.gamma(p) * sci.polygamma(1, p)))))

print(counter)   
plt.axis("equal")
plt.show()


