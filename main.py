import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def obrot(x,y,osx,osy,alfa):
    x = (x - osx) * np.cos(alfa) - (y - osy) * np.sin(alfa) + osx
    y = (x - osx) * np.sin(alfa) + (y - osy) * np.cos(alfa) + osy
    return x, y

x = np.linspace(0,30,1000)
wzor_funkcji = input("Enter function of argument x (in python convention eg. np.sin(x), 2*x): ")
f = lambda x: eval(wzor_funkcji)
y = f(x)
z = np.zeros(y.size)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim(0,30)
ax.set_zlim(-5,10)
z = np.linspace(-1, 1, 2)
X, Z = np.meshgrid(x,z)
Y = f(X)
funkcja = ax.plot_surface(X,Z,Y)
xa, ya = eval(input("Enter first corner coordinates, separated by comma: "))
xb, yb = eval(input("Enter second corner coordinates (adjacent to corner 1), separated by comma: "))
xc, yc = eval(input("Enter third corner coordinates (adjacent to corner 2), separated by comma: "))
xd, yd = eval(input("Enter fourth corner coordinates (adjacent to corner 3), separated by comma: "))
if(ya<f(xa)):
    yb = yb + f(xa) - ya
    yc = yc + f(xa) - ya
    yd = yd + f(xa) - ya
    ya = f(xa)
figura, = ax.plot(0,0)
sladx = []
slady = []
sladz = []
slad, = ax.plot(0,0)
lklatek = 1000
os = 1
prevos = 0
def frame(i):
    global os, prevos, xa,ya,xb,yb,xc,yc,xd,yd
    alfa = -np.pi / 200
    if(os == 1): # point a axis
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
    elif (os == 2):  # point b axis
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
    elif (os == 3):  # point c axis
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
    elif (os == 4):  # point d axis
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

    figura.set_xdata([xa,xb,xc,xd,xa])
    figura.set_ydata(np.zeros(5))
    figura.set_3d_properties([ya,yb,yc,yd,ya])
    xdat = [xa,xb,xc,xd,xa]
    ydat = np.linspace(-1, 0, 2)
    zdat = np.array([[ya,yb,yc,yd,ya],[ya,yb,yc,yd,ya]])
    Xdat, Ydat = np.meshgrid(xdat,ydat)

    sladx.append(xa)
    slady.append(ya)
    sladz.append(-1)
    slad.set_data(sladx,sladz)
    slad.set_3d_properties(slady)
    ax.clear()
    ax.set_xlim(0,30)
    ax.set_zlim(-5,10)
    ax.set_ylim(-5,5)
    ax.plot_surface(X,Z,Y)
    ax.plot_surface(Xdat,Ydat,zdat)
    ax.plot(sladx,sladz,slady)

if __name__ == "__main__":
    animation = anim.FuncAnimation(fig, frame, frames=lklatek, interval=1)
    plt.show()
