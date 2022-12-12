import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def funkcja(x):
    return 10*np.sin(x/5)
#    return x**2 /10

#func_formula = input("Wpisz wzór funkcji: ")

#funkcja = lambda x: eval(func_formula)

#x = np.linspace(0,20,21)
#normalna funkcja
#x = np.arange(-10,10, np.pi/100)
#y = funkcja(x)
param = np.linspace(0,2*np.pi,1000)
x = 8*np.cos(param)
y = 5*np.sin(param)
dx = np.diff(x)
dy = np.diff(y)
katnach = np.arctan2(dy,dx)
#pochodna = np.gradient(y,x)
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
#ax.set_ylim(-4, 4)
#if(funkcja(10) < funkcja(0) -1 ):
#    ax.invert_yaxis()
#ax.set_aspect('equal')

line, = ax.plot(x,y)
kolo, = ax.plot(0,0)
promien, = ax.plot(0,0)
sladx = []
slady = []
slad, = ax.plot(0,0)
dzielnik = 50
def frame(i):

    #t = np.arange(0, 2*3.1416, 0.03)
    t = np.linspace(0, 2*3.1416, 6)
    r=1
    krokx = x[i]
    kroky = y[i]
    korekcjax = -r*np.sin(katnach[i])
    korekcjay = r*np.cos(katnach[i])
    #krokxprev = krokx
    #krokyprev = kroky
    kat = - np.pi * i / dzielnik
    xokregu = r*np.cos(t+kat) + krokx + korekcjax
    yokregu = r*np.sin(t+kat) + kroky + korekcjay
    kolo.set_xdata(xokregu)
    kolo.set_ydata(yokregu)

    xwodz = r*np.cos(kat) + krokx + korekcjax
    ywodz = r*np.sin(kat) + kroky + korekcjay
    promien.set_xdata([krokx + korekcjax, xwodz])
    promien.set_ydata([kroky + korekcjay, ywodz])
    sladx.append(xwodz)
    slady.append(ywodz)
    slad.set_data(sladx, slady)
    return kolo, promien, slad

animation = animation.FuncAnimation(fig, frame, frames=np.arange(len(x) - 1), interval=1, repeat=False)
plt.show()
