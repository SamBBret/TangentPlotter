from base64 import b16decode
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci

class Vector3:
    __slots__ = ("x", "y", "s")

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s


xlenght = 1000

ylenght = 800
y1lenght = 802

halfnailwidth = 0.6 / 2

a2 = (ylenght - y1lenght)/(-xlenght - xlenght)
a4 = (-y1lenght + ylenght)/(xlenght + xlenght)

b2 = y1lenght/2 - a2 * xlenght/2
b4 = -ylenght/2 - a4 * -xlenght/2

zoom = 0.0065
#functionlimit = 7.98
functionlimit = 3.14 / 2

p = - functionlimit
increment = 1/50
fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')


coord_to_mm  = 1 / zoom / 2

string_lenght = 0

state = {'index': 0}
lines = []

last_line = None

print("0-gamma")
print("1-sin")

#functiontoDraw = input("Function to draw:")

while(p < functionlimit):

    points = []
    #a = sci.digamma(p) * sci.gamma(p)
    #b = sci.gamma(p) - a * p
    a = math.tan(p)
    b = 0

    b *= coord_to_mm

    d = a * (-xlenght/2) + b
    if abs(d) <= ylenght/2:
        points.append(Vector3(-xlenght/2, d, 3))

    d = a * xlenght/2 + b
    if abs(d) <= y1lenght/2:
        points.append(Vector3(xlenght/2, d, 1))

    d = (b2 - b) / (a - a2)  
    if abs(d) <= xlenght/2:
        points.append(Vector3(d, a*d + b, 2))
    d = (b4 - b) / (a - a4)
    if abs(d) <= xlenght/2:
        points.append(Vector3(d, a*d + b, 4))

    if len(points) != 0:
     
        lines.append(points)

    string_lenght += np.sqrt(np.pow(lines[-1][0].x - lines[-1][1].x, 2) + np.pow(lines[-1][0].y - lines[-1][1].y, 2))

    c = (0.2 + abs(1/(1 + a**2) * (a + (sci.gamma(p) * sci.polygamma(1, p)))))
    
    dp = increment / c

    a = sci.digamma(p + dp) * sci.gamma(p + dp)

    c1 = (0.2 + abs(1/(1 + (a)**2) * (a + (sci.gamma(p + dp) * sci.polygamma(1, p + dp)))))

    #p += increment / ((c + c1) / 2)
    p += 0.07


plt.axis("equal")  
print(len(lines))
print(str (string_lenght / 1000) + "m")


def draw_line():
    global last_line
    if len(lines) >  state['index']:

        if last_line is not None:
            last_line.set_color("black")
            last_line.set_linewidth("0.2")

        last_line, = ax.plot([lines[state['index']][0].x, lines[state['index']][1].x], [lines[state['index']][0].y, lines[state['index']][1].y], color="red", linewidth="0.6")
        print(str(state['index']) + ":")
        for point in lines[state['index']]:
            if point.s == 2:
                print("Ponto " + str(point.s) + ":   " + str(round(((xlenght / 2) - point.x) * (1002/xlenght) + 0.5, 2)) + "     " + str(round((point.y + (y1lenght / 2)) * (801/ylenght) + 0.5, 2)))
            elif point.s == 3:
                print("Ponto " + str(point.s) + ":   " + str(round((point.x + (xlenght / 2)) * (1002/xlenght) + 0.5, 2)) + "     " + str(round(((ylenght / 2) - point.y) * (801/ylenght) + 0.5, 2)))
            else:
                print("Ponto " + str(point.s) + ":   " + str(round((point.x + (xlenght / 2)) * (1002/xlenght) + 0.5, 2)) + "     " + str(round((point.y + (y1lenght / 2)) * (804/y1lenght) + 0.5, 2)))
    state['index'] += 1

def on_key(event):
    if event.key == " ":
        draw_line()
        plt.draw()
    if event.key == "a":
        printall()

def printall():
    while state['index'] < len(lines) :
        draw_line()
    print(len(lines))
    print(str (string_lenght / 1000) + "m")
    plt.draw()


#printall()

ax.set_xlim((-(xlenght)/2 - 20), ((xlenght)/2 + 20))
ax.set_ylim((-(max(y1lenght, ylenght))/2 - 20), ((max(y1lenght, ylenght)/2 + 20)))
ax.set_aspect('equal', adjustable='box')
fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()

