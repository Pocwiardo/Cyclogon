import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def funkcja(x):
    return 10*np.sin(x/5)
#    return x**2 /10

#func_formula = input("Enter the function formula: ")

# create a lambda function from the formula
#funkcja = lambda x: eval(func_formula)

#x = np.linspace(0,20,21)
x = np.arange(-10,10, np.pi/100)
y = funkcja(x)
dx = np.diff(x)
dy = np.diff(y)
katnach = np.arctan2(dy,dx)
#pochodna = np.gradient(y,x)
fig, ax = plt.subplots()
#ax.set_xlim(0, 10)
#ax.set_ylim(funkcja(0), funkcja(10))
#ax.set_ylim(-4, 4)
#if(funkcja(10) < funkcja(0) -1 ):
#    ax.invert_yaxis()
#ax.set_aspect('equal')

line = ax.plot(x,y)
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
    xokregu = r*np.cos(t) + krokx + korekcjax
    yokregu = r*np.sin(t) + kroky + korekcjay
    kolo.set_xdata(xokregu)
    kolo.set_ydata(yokregu)
    kat = - np.pi * i/dzielnik
    xwodz = r*np.cos(kat) + krokx + korekcjax
    ywodz = r*np.sin(kat) + kroky + korekcjay
    promien.set_xdata([krokx + korekcjax, xwodz])
    promien.set_ydata([kroky + korekcjay, ywodz])
    sladx.append(xwodz)
    slady.append(ywodz)
    slad.set_data(sladx, slady)
    return kolo, promien, slad

animation = animation.FuncAnimation(fig, func=frame, frames=np.arange(len(x) - 1), interval=1, repeat=False)
plt.show()