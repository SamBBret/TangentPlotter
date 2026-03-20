import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci

class Vector2:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


xsectors = 500
ysectors = 400

xreallenght = 1000

halfnailwidth = 0.6 / 2

zoom = 0.013
functionlimit = 7.99
uplimit = ysectors*zoom
sidelimit = xsectors*zoom 
p = -7.99
increment = 1/40
fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')



sectors_to_mm = xreallenght / xsectors
coord_to_mm  = xreallenght / sidelimit / 2
coord_to_sectors = xsectors / sidelimit / 2

string_lenght = 0

state = {'index': 0}
lines = []

print("0-gamma")
print("1-sin")

functiontoDraw = input("Function to draw:")

while(p < functionlimit):

    points = []
    a = sci.digamma(p) * sci.gamma(p)
    b = sci.gamma(p) - a * p

    c = (0.25 + abs(1/(1 + a**2) * (a + (sci.gamma(p) * sci.polygamma(1, p)))))

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

    p += increment / c

for line in lines:
    for p in line:
        if p.x == -sidelimit:
            p.x = p.x * coord_to_mm
            p.y = p.y * coord_to_sectors 
            if p.y - round(((p.y / ysectors) + 0.5) * ysectors) + ysectors/2 + .5 >= 1 - halfnailwidth:
            
                p.y = round(((p.y / ysectors) + 0.5) * ysectors - (ysectors/2)) * sectors_to_mm

            elif p.y - round(((p.y /( 2 * uplimit)) + 0.5) * ysectors) + ysectors/2 + .5 <  .5 - halfnailwidth:

                 p.y = ((round(((p.y / ysectors) + 0.5) * ysectors) + 1 - (ysectors/2)) * sectors_to_mm)
                 
            else:
                
                 p.y = ((round(((p.y / ysectors) + 0.5) * ysectors) + (1 - halfnailwidth * 2) - (ysectors/2)) * sectors_to_mm)
                 

        elif p.x == sidelimit:
            p.x = p.x * coord_to_mm
            p.y = p.y * coord_to_sectors 
            if p.y - round(((p.y / ysectors) + 0.5) * ysectors) + ysectors/2 + .5 < halfnailwidth:
            
                p.y = round(((p.y / ysectors) + 0.5) * ysectors - (ysectors/2)) * sectors_to_mm

            elif p.y - round(((p.y /( 2 * uplimit)) + 0.5) * ysectors) + ysectors/2 + .5 >=  .5 + halfnailwidth:

                 p.y = ((round(((p.y / ysectors) + 0.5) * ysectors) + 1 - (ysectors/2)) * sectors_to_mm)
             
            else:
                
                 p.y = ((round(((p.y / ysectors) + 0.5) * ysectors) + (halfnailwidth * 2) - (ysectors/2)) * sectors_to_mm)
                 
        
                 
        elif p.y == uplimit:
            p.y = p.y * coord_to_mm
            p.x = p.x * coord_to_sectors
            if p.x - round(((p.x / xsectors) + 0.5) * xsectors) + xsectors/2 + .5 >= 1 - halfnailwidth:

                p.x = (round(((p.x / xsectors) + 0.5) * xsectors - (xsectors/2)) * sectors_to_mm)

            elif p.x - round(((p.x / xsectors) + 0.5) * xsectors) + xsectors/2 + .5 < .5 - halfnailwidth:

                 p.x = ((round(((p.x / xsectors) + 0.5) * xsectors) + 1 - (xsectors/2)) * sectors_to_mm)

            else:
                
                 p.x = ((round(((p.x / xsectors) + 0.5) * xsectors) + (1 - halfnailwidth * 2) - (xsectors/2)) * sectors_to_mm)
 
        else:
            p.y = p.y * coord_to_mm
            p.x = p.x * coord_to_sectors

            #p.y = p.y - ((5/1000) * (p.x + 500))


            if p.x - round(((p.x / xsectors) + 0.5) * xsectors) + xsectors/2 + .5 < halfnailwidth:

                p.x = (round(((p.x / xsectors) + 0.5) * xsectors - (xsectors/2)) * sectors_to_mm)

            elif p.x - round(((p.x / xsectors) + 0.5) * xsectors) + xsectors/2 + .5 >= .5 + halfnailwidth:

                 p.x = ((round(((p.x / xsectors) + 0.5) * xsectors) + 1 - (xsectors/2)) * sectors_to_mm)

            else:
                
                 p.x = ((round(((p.x / xsectors) + 0.5) * xsectors) + (halfnailwidth * 2) - (xsectors/2)) * sectors_to_mm)
    string_lenght += np.sqrt(np.pow(line[0].x - line[1].x, 2) + np.pow(line[0].y - line[1].y, 2))


plt.axis("equal")  
print(len(lines))
print(str (string_lenght / 1000) + "m")


def draw_line():
    if len(lines) >  state['index']:
        ax.plot([lines[state['index']][0].x, lines[state['index']][1].x], [lines[state['index']][0].y, lines[state['index']][1].y], color="black", linewidth="0.2")
        plt.draw()
        print(str(state['index']) + ":")
        print("Ponto 0:   " + str(round(lines[state['index']][0].x)) + "     " + str(round(lines[state['index']][0].y)))
        print("Ponto 1:   " + str(round(lines[state['index']][1].x)) + "     " + str(round(lines[state['index']][1].y)))

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

