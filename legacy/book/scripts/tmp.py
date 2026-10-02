from pylab import *

# create signal
def create_signal(fs,N):
	""" create signal with gaussian noise"""
	dt = 1./fs
	t = linspace(0,N*dt,N)
	y = 1.0*sin(2*pi*10*t) + 1.5*sin(2*pi*35.7*t)
	noise=normal(0,1,N)  #mean, std dev, num pts
	sig=y+noise
	plot(t,sig,'b-')
	show()
	return t,sig

