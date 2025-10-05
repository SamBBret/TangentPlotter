import numpy as np
import matplotlib.pyplot as plt

functionlimit = 5*np.pi
uplimit = 5*np.pi
sidelimit = 6*np.pi
p = 0-functionlimit
increment = 1/30
plt.figure(figsize=(5, 5), layout='constrained')

while(p < functionlimit):
    xpoint = []
    ypoint = []
    a = 1 - ((p**2) / 2) + ((p**4) / 24)
    b = (2 * (p**3) / 6) - (4 * (p**5) / 120)
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
    p += increment / (0.1 + abs(1/(1 + a**2) * (-np.sin(p))))
    
plt.axis("equal")
plt.show()


