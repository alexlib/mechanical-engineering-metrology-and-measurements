# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## Hysteresis example
# 
# Given calibration of an instrument for an increasing and decreasing input $x$ [mV] and output of the instrument $y$ [mV]
# 

# <codecell>

import numpy as np
import pylab as pl

# <codecell>

from IPython.core.display import Image 
Image(filename='hysteresis_example.png')

# <codecell>

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0])
y = np.array([0.1, 1.1, 2.1, 3.0, 4.1, 5.0, 5.0, 4.2, 3.2, 2.2, 1.2, 0.2])

# <codecell>

pl.plot(x,y,'o')
pl.xlabel('$x$ [mV]')
pl.ylabel('$y$ [mV]')

# <markdowncell>

# 1. We see the error, but we do not know if it is a random or not
# 2. In order to see the hysteresis, we have to set the plot with the lines connecting points:

# <codecell>

pl.plot(x,y,'--o')
pl.xlabel('$x$ [mV]')
pl.ylabel('$y$ [mV]')

# <markdowncell>

# ### Estimate the hysteresis error:
# 
# $e_h = y_{up} - y_{down}$
# 
# $e_{h_{max}} = max(|e_h|)$
# 
# $e_{h_{max}}\% = 100\% \cdot \frac{e_{h_{max}}}{y_{max}-y_{min}} $

# <codecell>

e_h = y[:6]-np.flipud(y[6:]) 
print "e_h =", e_h,"[mV]"

# <codecell>

e_hmax = np.max(np.abs(e_h))
print "e_hmax= %3.2f %s" % (e_hmax,"[mV]")

# <codecell>

e_hmax_p = 100*e_hmax/(np.max(y) - np.min(y))
print "Relative error = %3.2f%s FSO" % (e_hmax_p,"%")

# <markdowncell>

# # Sensitivity error example

# <codecell>

from IPython.core.display import Image 
Image(filename='sensitivity_error_example.png') 

# <codecell>

x = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0])
y = np.array([0.4, 1.0, 2.3, 6.9, 15.8, 36.4, 110.1, 253.2])

# <codecell>

pl.plot(x,y,'--o')
pl.xlabel('$x$ [cm]')
pl.ylabel('$y$ [V]')
pl.title('Calibration curve')

# <markdowncell>

# Sensitivity, $K$ is:
# 
# $ K_i  = \left( \frac{\partial y}{\partial x} \right)_{x_i} $

# <codecell>

K = np.diff(y)/np.diff(x)
print K

# <codecell>


# <codecell>


# <codecell>

pl.plot(x[1:],K,'--o')
pl.xlabel('$x$ [cm]')
pl.ylabel('$K$ [V/cm]')
pl.title('Sensitivity')

# <markdowncell>

# Instead of working with non-linear curve of sensitivity we can use the usual trick: the logarithmic scale

# <codecell>

pl.loglog(x,y,'--o')
pl.xlabel('$x$ [cm]')
pl.ylabel('$y$ [V]')
pl.title('Logarithmic scale')

# <codecell>

logK = np.diff(np.log(y))/np.diff(np.log(x))
print logK
pl.plot(x[1:],logK,'--o')
pl.xlabel('$x$ [cm]')
pl.ylabel('$K$ [V/cm]')
pl.title('Logarithmic sensitivity')
pl.hold(True)
pl.plot([x[1],x[-1]],[1.2,1.2],'r--')

# <codecell>

pl.loglog(x,y,'o',x,x**(1.2))
pl.xlabel('$x$ [cm]')
pl.ylabel('$y$ [V]')
pl.title('Logarithmic scale')
pl.legend(('$y$','$x^{1.2}$'),loc='best')

# <codecell>

pl.plot(x,y-x**(1.2),'o')
pl.xlabel('$x$ [cm]')
pl.ylabel('$y - y_c$ [V]')
pl.title('Deviation plot')
# pl.legend(('$y$','$x^{1.2}$'),loc='best')

# <markdowncell>

# ## Regression analysis
# Following the recipe of http://www.answermysearches.com/how-to-do-a-simple-linear-regression-in-python/124/

# <codecell>

from math import sqrt
def linreg(X, Y):
    """
    Summary
        Linear regression of y = ax + b
    Usage
        real, real, real = linreg(list, list)
    Returns coefficients to the regression line "y=ax+b" from x[] and y[], and R^2 Value
    """
    if len(X) != len(Y):  raise ValueError, 'unequal length'
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in map(None, X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    a, b = (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det
    meanerror = residual = 0.0
    for x, y in map(None, X, Y):
        meanerror = meanerror + (y - Sy/N)**2
        residual = residual + (y - a * x - b)**2
    RR = 1 - residual/meanerror
    ss = residual / (N-2)
    Var_a, Var_b = ss * N / det, ss * Sxx / det
    #print "y=ax+b"
    #print "N= %d" % N
    #print "a= %g \\pm t_{%d;\\alpha/2} %g" % (a, N-2, sqrt(Var_a))
    #print "b= %g \\pm t_{%d;\\alpha/2} %g" % (b, N-2, sqrt(Var_b))
    #print "R^2= %g" % RR
    #print "s^2= %g" % ss
    return a, b, RR

# <codecell>

print linreg(np.log(x),np.log(y))

# <codecell>

pl.loglog(x,y,'o',x,x**(1.21)-0.0288)
pl.xlabel('$x$ [cm]')
pl.ylabel('$y$ [V]')
pl.title('Logarithmic scale')
pl.legend(('$y$','$x^{1.2}$'),loc='best')

# <codecell>

pl.plot(x,y-(x**(1.21)-0.0288),'o')
pl.xlabel('$x$ [cm]')
pl.ylabel('$y - y_c$ [V]')
pl.title('Deviation plot')
# pl.legend(('$y$','$x^{1.2}$'),loc='best')

# <codecell>


