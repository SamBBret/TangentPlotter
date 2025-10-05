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
    a = np.cos(p)
    c = np.sin(p) - a * p
    b = a * (-sidelimit) + c
    if abs(b) <= uplimit:
        xpoint.append(-sidelimit)
        ypoint.append(b)
    b = a * sidelimit + c
    if abs(b) <= uplimit:
        xpoint.append(sidelimit)
        ypoint.append(b)
    b = (-uplimit - c) / a
    if abs(b) < sidelimit:
        xpoint.append(b)
        ypoint.append(-uplimit)
    b = (uplimit - c) / a
    if abs(b) < sidelimit:
        xpoint.append(b)
        ypoint.append(uplimit)

    plt.plot(xpoint, ypoint, color="black", linewidth="0.2")
    p += increment / (0.1 + abs(1/(1 + a**2) * (-np.sin(p))))
    
plt.axis("equal")
plt.show()

