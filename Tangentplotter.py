import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci

zoom = 0.8
functionlimit = 7*np.pi
uplimit = 8*zoom
sidelimit = 10*zoom 
p = -7.99
increment = 1/30
fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')

state = {'index': 0}
lines = []

while(p < functionlimit):

    xpoint = []
    ypoint = []
    a = sci.digamma(p) * sci.gamma(p)
    b = sci.gamma(p) - a * p
    c = (0.25 + abs(1/(1 + a**2) * (a + (sci.gamma(p) * sci.polygamma(1, p)))))
    d = a * (-sidelimit) + b
    if abs(d) <= uplimit:
        xpoint.append(-sidelimit)
        ypoint.append(d)
    d = a * sidelimit + b
    if abs(d) <= uplimit:
        xpoint.append(sidelimit)
        ypoint.append(d)
    d = (-uplimit - b) / a
    if abs(d) < sidelimit:
        xpoint.append(d)
        ypoint.append(-uplimit)
    d = (uplimit - b) / a
    if abs(d) < sidelimit:
        xpoint.append(d)
        ypoint.append(uplimit) 

    lines.append([xpoint, ypoint])
    p += increment / c

plt.axis("equal")  
print(len(lines))

def on_key(event):
    if event.key == " " and len(lines) >  state['index']:
        ax.plot(lines[state['index']][0], lines[state['index']][1], color="black", linewidth="0.2")
        plt.draw()
        print(str(state['index']) + ": \n" + str(lines[state['index']]))
        state['index'] += 1

ax.set_xlim(-sidelimit - 1, sidelimit + 1)
ax.set_ylim(-uplimit - 1, uplimit + 1)
ax.set_aspect('equal', adjustable='box')
fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()

