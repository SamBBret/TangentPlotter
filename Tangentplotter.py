import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci

class Vector2:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


xreallenght = 1002
yreallenght = 802

xsectors = 501
ysectors = xsectors * yreallenght / xreallenght

halfnailwidth = 0.6 / 2

zoom = 0.013
functionlimit = 7.98
uplimit = ysectors*zoom
sidelimit = xsectors*zoom 
p = -7.98
increment = 1/50
fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')



sectors_to_mm = xreallenght / xsectors
coord_to_mm  = xreallenght / sidelimit / 2
coord_to_sectors = xsectors / sidelimit / 2

string_lenght = 0

state = {'index': 0}
lines = []

print("0-gamma")
print("1-sin")

#functiontoDraw = input("Function to draw:")

while(p < functionlimit):

    points = []
    a = sci.digamma(p) * sci.gamma(p)
    b = sci.gamma(p) - a * p

    d = a * (-sidelimit) + b
    if abs(d) <= uplimit:
        points.append(Vector2(-sidelimit, d))

    d = a * sidelimit + b
    if abs(d) <= uplimit:
        points.append(Vector2(sidelimit, d))

    d = (-uplimit - b) / a
    if abs(d) < sidelimit:
        points.append(Vector2(d, -uplimit))

    d = (uplimit - b) / a
    if abs(d) < sidelimit:
        points.append(Vector2(d, uplimit))

    if len(points) != 0:
     
        lines.append(points)

    c = (0.2 + abs(1/(1 + a**2) * (a + (sci.gamma(p) * sci.polygamma(1, p)))))
    
    dp = increment / c

    a = sci.digamma(p + dp) * sci.gamma(p + dp)

    c1 = (0.2 + abs(1/(1 + (a)**2) * (a + (sci.gamma(p + dp) * sci.polygamma(1, p + dp)))))

    p += increment / ((c + c1) / 2)


for line in lines:
    for p in line:
        p.x = p.x * coord_to_mm
        p.y = p.y * coord_to_mm
 
    string_lenght += np.sqrt(np.pow(line[0].x - line[1].x, 2) + np.pow(line[0].y - line[1].y, 2))


plt.axis("equal")  
print(len(lines))
print(str (string_lenght / 1000) + "m")


def draw_line():
    if len(lines) >  state['index']:
        ax.plot([lines[state['index']][0].x, lines[state['index']][1].x], [lines[state['index']][0].y, lines[state['index']][1].y], color="black", linewidth="0.2")
        plt.draw()
        print(str(state['index']) + ":")
        print("Ponto 0:   " + str(round(lines[state['index']][0].x + (xreallenght / 2), 1)) + "     " + str(round(lines[state['index']][0].y + (yreallenght / 2), 1)))
        print("Ponto 1:   " + str(round(lines[state['index']][1].x + (xreallenght / 2), 1)) + "     " + str(round(lines[state['index']][1].y + (yreallenght / 2), 1)))

    state['index'] += 1

def on_key(event):
    if event.key == " ":
        draw_line()
    if event.key == "a":
        while state['index'] < len(lines) :
            draw_line()
        print(len(lines))
        print(str (string_lenght / 1000) + "m")

ax.set_xlim((-(xsectors * sectors_to_mm)/2 - 20), ((xsectors * sectors_to_mm)/2 + 20))
ax.set_ylim((-(ysectors * sectors_to_mm)/2 - 20), ((ysectors * sectors_to_mm)/2 + 20))
ax.set_aspect('equal', adjustable='box')
fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()

