from pylab import *
from scipy import signal

# Define transfer function
k = 1 		# sensitivity
wn = 546.72 # rad/s
z=0.467     # damping

sys = signal.lti(k*wn**2,[1,2*z*wn, wn**2])
plot(arange(1000)/wn,sys.step(N=1000)[1])
title('Step response')
xlabel('$t$ [sec]')
ylabel('E [V]')
show()
