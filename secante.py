from math import *

xi_1=-5
xi=5

def f(x):
    return x**2+3*x+2-exp(x)

ant=0
for i in range(1,1000):

    fi_1=f(xi_1)
    fi=f(xi)
    xi_2=xi-(fi*(xi_1-xi)/(fi_1-fi))
    ea=abs((ant-xi_2)/xi_2)*100
    ant=xi_2
    print("{0} {1} {2} {3} {7}".format(i,xi,xi_1,xi_2,fi_1,fi,xi_2,ea))
    xi_1=xi
    xi=xi_2
    
    if ea<10**-5:
        break