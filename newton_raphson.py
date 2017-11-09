from math import *

xi=-5

def f(x):
    return x**2+3*x+2-exp(x)
def f_d(x):
    return 2*x+3-exp(x)

ant=0
for i in range(1,1000):
    fi=f(xi)
    fi_d=f_d(xi)
    xi=xi-(fi/fi_d)
    ea=abs((ant-xi)/xi)*100
    ant=xi
    print("{0} {1} {2}".format(i,xi,ea))

    
    if ea<10**-5:
        break