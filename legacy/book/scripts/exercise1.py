""" Exercise 1
Statistical measures of a small sample
"""
from pylab import *

x = array([12.1,12.3,12.2,12.2,12.4,12.3,12.2,12.4,12.2,12.5])
x_mean = mean(x)
x_median = median(x)
x_variance = var(x)
x_std = std(x)
x_modes = hist(x)
show()
x_mode_ind = argmax(x_modes[0])
x_mode_count = x_modes[0][x_mode_ind]
x_mode_val = x[x_mode_ind]
print "Data:"; print x
print "Mean: %f " % x_mean
print "Median: %f" % x_median
print "Variance: %f" % x_variance
print "STD: %f " % x_std
print "Mode of x %f appears %d times" % (x_mode_val,x_mode_count)

