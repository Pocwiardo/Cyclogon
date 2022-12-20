import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def obrot(x,y,osx,osy,alfa):
    x = (x - osx) * np.cos(alfa) - (y - osy) * np.sin(alfa) + osx
    y = (x - osx) * np.sin(alfa) + (y - osy) * np.cos(alfa) + osy
    return x, y

x = np.linspace(-10,20,1000)
wzor_funkcji = input("Wpisz wzór funkcji od argumentu x: ")
f = lambda x: eval(wzor_funkcji)
y = f(x)
fig, ax = plt.subplots()
ax.set_xlim(-5,20)
ax.set_ylim(-5,10)
funkcja = ax.plot(x,y)
xa, ya = eval(input("Podaj punkt 1, który będzie zakreślać cyklogon: "))
xb, yb = eval(input("Podaj punkt 2, sąsiedni do punktu 1: "))
xc, yc = eval(input("Podaj punkt 3, sąsiedni do punktu 2: "))
xd, yd = eval(input("Podaj punkt 4, sąsiedni do punktu 3: "))
#xa, xb, xc, xd = 0, 0, 2, 1
#ya, yb, yc, yd = 0, 1, 1, 0
if(ya<f(xa)):
    yb = yb + f(xa) - ya
    yc = yc + f(xa) - ya
    yd = yd + f(xa) - ya
    ya = f(xa)
figura, = ax.plot(0,0)
sladx = []
slady = []
slad, = ax.plot(0,0)
lklatek = 1000
os = 1
prevos = 0
def frame(i):
    global os, prevos, xa,ya,xb,yb,xc,yc,xd,yd
    alfa = -np.pi / 1000
    if(os == 1): # punkt a osią
        xb, yb = obrot(xb, yb, xa, ya, alfa)
        xc, yc = obrot(xc, yc, xa, ya, alfa)
        xd, yd = obrot(xd, yd, xa, ya, alfa)
        if(yb<=f(xb) and prevos != 2):
            os = 2
            prevos = 1
        elif(yc<=f(xc) and prevos != 3):
            os = 3
            prevos = 1
        elif(yd<=f(xd) and prevos != 4):
            os = 4
            prevos = 1
    elif (os == 2):  # punkt b osią
        xa, ya = obrot(xa, ya, xb, yb, alfa)
        xc, yc = obrot(xc, yc, xb, yb, alfa)
        xd, yd = obrot(xd, yd, xb, yb, alfa)
        if (ya <= f(xa) and prevos != 1):
            os = 1
            prevos = 2
        elif (yc <= f(xc) and prevos != 3):
            os = 3
            prevos = 2
        elif (yd <= f(xd) and prevos != 4):
            os = 4
            prevos = 2
    elif (os == 3):  # punkt c osią
        xa, ya = obrot(xa, ya, xc, yc, alfa)
        xb, yb = obrot(xb, yb, xc, yc, alfa)
        xd, yd = obrot(xd, yd, xc, yc, alfa)
        if (ya <= f(xa) and prevos != 1):
            os = 1
            prevos = 3
        elif (yb <= f(xb) and prevos != 2):
            os = 2
            prevos = 3
        elif (yd <= f(xd) and prevos != 4):
            os = 4
            prevos = 3
    elif (os == 4):  # punkt d osią
        xa, ya = obrot(xa, ya, xd, yd, alfa)
        xb, yb = obrot(xb, yb, xd, yd, alfa)
        xc, yc = obrot(xc, yc, xd, yd, alfa)
        if (ya <= f(xa) and prevos != 1):
            os = 1
            prevos = 4
        elif (yb <= f(xb) and prevos != 2):
            os = 2
            prevos = 4
        elif (yc <= f(xc) and prevos != 3):
            os = 3
            prevos = 4

    figura.set_data([xa,xb,xc,xd,xa],[ya,yb,yc,yd,ya])
    sladx.append(xa)
    slady.append(ya)
    slad.set_data(sladx,slady)
    return slad, figura

animation = anim.FuncAnimation(fig, frame, frames=lklatek, interval=10)


plt.show()
