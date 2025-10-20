
# coding: utf-8

# ## Exercise 1: Statistics of a small sample - histogram

# In[28]:

from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

get_ipython().magic(u'pylab inline')

x = array([12.1,12.3,12.2,12.2,12.4,12.3,12.2,12.4,12.2,12.5])
# show the histogram
x_modes = hist(x)


# In[29]:

x_mode_ind = argmax(x_modes[0])
x_mode_count = x_modes[0][x_mode_ind]
x_mode_val = x[x_mode_ind]
print "Data:"; print x
print "Mean: %f " % mean(x)
print "Median: %f" % median(x)
print "Variance: %f" % var(x)
print "STD: %f " % std(x)
print "Mode of x %f appears %d times" % (x_mode_val,x_mode_count)


# ## What is this histogram in the first place? 

# In[30]:

# Simplest historam
import numpy as np



nbins = 10
data = x.copy()

hist_vals = np.zeros(nbins)
min_val = data.min()
max_val = data.max() + .1
for d in data:
    bin_number = int(nbins * ((d - min_val) / (max_val - min_val)))
    hist_vals[bin_number] += 1
    
plt.stem(np.linspace(min_val,max_val,nbins),hist_vals)
plt.xlim([min_val-.1,max_val+.1])
plt.show()

