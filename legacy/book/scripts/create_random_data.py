from random import random
def create_random_set(N=6):
    """ creates random data set of concentration versus temperature """
    c = []
    w = []
    T = []
    k = random()*0.05
    b = random()*0.002

    for i in range(N):
        c.append(random()*55)
        w.append(random()*10)

    c.sort()

    T = []
    for i in range(N):
        T.append(100*10**(-(c[i]*k + b))+ w[i])


    return c,T