""" Exercise 2
Histogram, normalized histogram, probability density function"""

from pylab import *

data = loadtxt('thermocouples.dat',skiprows=1)
fig = figure()
plot(data[:,0],data[:,1])
xlabel('n')
ylabel('T [$^\circ$ C]')
show()

fig = figure()
hist(data[:,1],bins=2*len(data[:,1])**(0.333))
show()





