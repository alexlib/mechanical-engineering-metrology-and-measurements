
# coding: utf-8

# In[29]:

data = loadtxt('thermocouples.dat',skiprows=1)
t = data[:,0]
T = data[:,1]
plot(t,T)
xlabel('$t$ [sec]')
ylabel(r'$T^\circ$C') 
display()


# In[30]:

print 1 + 3.3*log10(len(t))
print 2*len(t)**(0.33)


# In[31]:

J = 11
n,bins,patches = hist(T,J)
x = bins[:-1]+0.5*diff(bins)[0]
plot(x,n,'r')
xlabel(r'$T^\circ$C')
ylabel('Counts')
title('11 bins')


# In[32]:

J = 19
n,bins,patches = hist(T,J)
x = bins[:-1]+0.5*diff(bins)[0]
plot(x,n,'r')
xlabel(r'$T^\circ$C')
ylabel('Counts')
title('19 bins')


# In[33]:

J = 15
n,bins,patches = hist(T,J)
x = bins[:-1]+0.5*diff(bins)[0]
plot(x,n,'r')
xlabel(r'$T^\circ$C')
ylabel('Counts')
title('15 bins')


# In[34]:

# vertical normalization
p = n/1000.
plot(x,p)
xlabel(r'$T^\circ$C')
ylabel('Relative counts')
title('Vertically normalized')


# In[35]:

# area normalization
f = p/diff(x)[0]
plot(x,f)
xlabel(r'$T^\circ$C')
ylabel('Probability Density')


# In[36]:

# horizontal normalization
z = (x - T.mean())/T.std()
plot(z,f)
xlabel(r'$x$ ')
ylabel(r'$P(x)$')
title('Final result')


# In[37]:

def gaussian(x,mu,sig):
    return 1/(sig*sqrt(2*pi))*exp(-((x-mu)**2)/(2*sig**2))

plot(z,f,z,gaussian(z,0,1),'r')
xlabel(r'$x$')
ylabel(r'$P(x)$')
title('Blue - original, red - Gaussian')


# In[38]:

import scipy.stats as st

print "T skewness = %f, kurtosis = %f" % (st.skew(T), st.kurtosis(T))
tmp = randn(1000,1)
print "Normal distribution skewness = %f, kurtosis = %f" % (st.skew(tmp), st.kurtosis(tmp))


# In[39]:

# area under the curve
print "Area under the curve = %f " % trapz(f,x)


# In[39]:



