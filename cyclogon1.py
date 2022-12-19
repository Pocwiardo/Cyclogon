import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

x = np.linspace(-10,10,100)
y = 0* x
fig, ax = plt.subplots()
ax.set_xlim(-10,20)
ax.set_ylim(-10,10)
funkcja = ax.plot(x,y)
#xa, ya = input("Podaj punkt 1: ").split(",")
#xb, yb = input("Podaj punkt 2: ").split(",")
#xc, yc = input("Podaj punkt 3: ").split(",")
#xd, yd = input("Podaj punkt 4: ").split(",")
xa, xb, xc, xd = 0, 0, 4, 4
ya, yb, yc, yd = 0, 4, 4, 0
figura = ax.plot([xa,xb,xc,xd,xa],[ya,yb,yc,yd,ya])
r1= np.sqrt((xa-xd)**2+(ya-yd)**2)
r2= np.sqrt((xd-xb)**2+(yd-yb)**2)
r3 =np.sqrt((xa-xb)**2+(ya-yb)**2)
sladx = []
slady = []
slad, = ax.plot(0,0)
lklatek = 100
def frame(i):
    alfa = np.pi * 3/2 * i/lklatek
    if(alfa < np.pi/2):
        xfig = -r1*np.cos(alfa) + xa + r1
        yfig = r1 * np.sin(alfa) + ya
    elif (alfa >= np.pi / 2 and alfa < np.pi):
        offsetal = -np.pi/4
        xfig = -r2 * np.cos(alfa+offsetal) + xa + + r1 + np.sqrt((xd-xc)**2+(yd-yc)**2)
        yfig = r2 * np.sin(alfa+offsetal) + ya
    elif (alfa >= np.pi and alfa < np.pi *3/2):
        offsetal = -np.pi/2
        xfig = -r3 * np.cos(alfa+offsetal) + xa + r1 +np.sqrt((xc-xb)**2+(yc-yb)**2) + np.sqrt((xd-xc)**2+(yd-yc)**2)
        yfig = r3 * np.sin(alfa+offsetal) + ya

    sladx.append(xfig)
    slady.append(yfig)
    slad.set_data(sladx,slady)
    return slad

animation = anim.FuncAnimation(fig, frame, frames=lklatek, interval=1)


plt.show()
