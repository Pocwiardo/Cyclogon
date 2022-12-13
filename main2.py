import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim


#x = np.arange(-10,10,np.pi/100)
#f = lambda x: x**3 / 200
#y = f(x)
a = np.linspace(-10,10,100)
b = np.full(100,10)
c = np.flip(a)
d = np.full(100,-10)
x = np.concatenate((a,b,c,d), axis = 0)
y = np.concatenate((b,c,d,a), axis = 0)
dx = np.diff(x)
dy = np.diff(y)
alfa = np.arctan2(dy,dx)
fig, ax = plt.subplots()
ax.set_xlim(-15,15)
ax.set_ylim(-15, 15)
funkcja = ax.plot(x,y)
figura, = ax.plot(0,0)
promien, = ax.plot(0,0)
slad, = ax.plot(0,0)
sladx = []
slady = []
def frame(i):
    omega = -np.pi * i/50
    movex = x[i]
    movey = y[i]
    tf = np.linspace(0, np.pi * 2, 5)
    r = 1
    offsetx = -r*np.sin(alfa[i])
    offsety = r * np.cos(alfa[i])
    xf = r*np.cos(tf + omega) + movex + offsetx
    yf = r*np.sin(tf + omega) + movey + offsety
    figura.set_data(xf,yf)
    xpromien = movex + offsetx + r*np.cos(omega)
    ypromien = movey + offsety + r*np.sin(omega)
    promien.set_data([movex + offsetx, xpromien],[movey + offsety, ypromien])
    sladx.append(xpromien)
    slady.append(ypromien)
    slad.set_data(sladx,slady)
    return figura, promien, slad
animacja = anim.FuncAnimation(fig, frame, frames = len(x)-1, interval = 0)
plt.show()
