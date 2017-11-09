from math import *

xi=-5
xu=5

def f(x):
    return x**2+3*x+2-exp(x)

ant=0
for i in range(1,1000):

    fu=f(xu)
    fi=f(xi)
    xr=xu-(fu*(xi-xu)/(fi-fu))
    fr=f(xr)
    ea=abs((ant-xr)/xr)*100
    ant=xr
    print("{0} {1} {2} {3} {7}".format(i,xi,xu,xr,fu,fi,fr,ea))
    if fi*fr>0:
        xi=xr
    else:
        xu=xr
    if ea<10**-5:
        break

