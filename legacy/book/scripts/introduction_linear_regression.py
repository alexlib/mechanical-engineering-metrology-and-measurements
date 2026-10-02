# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## Introduction to linear regression
# 
# Based on the example given in http://onlinestatbook.com/2/regression/intro.html

# <codecell>

%pylab inline 
# allows to use everything from Numpy and Matplotlib like in Matlab, without np. and plt.

from IPython.core.display import Image 
# allows to show images from the web: Image(filename='hysteresis_example.png',width=400)

# <codecell>

# Let's use some simple example of two variables, x,y
x = array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([1.0, 2.0, 1.30, 3.75, 2.25])

# <codecell>

plot(x,y,'o',markersize=10)
xlim([0.0, 6.0])
ylim([0.0, 4.0])
xlabel('$x$',fontsize=16)
ylabel('$y$',fontsize=16)

# <markdowncell>

# In simple linear regression, the topic of this section, the predictions of Y when plotted as a function of X form a straight line.
# Linear regression consists of finding the best-fitting straight line through the points. The best-fitting line is called a regression line. The black diagonal line in Figure 2 is the regression line and consists of the predicted score on Y for each possible value of X. The vertical lines from the points to the regression line represent the errors of prediction.

# <codecell>

Image(url='http://onlinestatbook.com/2/regression/graphics/reg_error.gif')

# <markdowncell>

# The error of prediction for a point is the value of the point minus the predicted value (the value on the line). Table 2 shows the predicted values (Y') and the errors of prediction (Y-Y'). For example, the first point has a Y of 1.00 and a predicted Y (called Y') of 1.21. Therefore, its error of prediction is -0.21.
# 
# The formula for the regression line is 
# 
# $$ y' = b \cdot x + a $$
# 
# Let's assume we try some values of $a,b$: 
# 
# $$ y' = 0.425\, x + 0.758 $$

# <codecell>

b = 0.425
a = 0.785

ytag = x*b + a
print "y'"
print ytag
print 'original y:'
print y

# <codecell>

e = ytag - y
print 'Errors:'
print e

# <markdowncell>

# ### Computing the Regression Line
# 
# In the age of computers, the regression line is typically computed with statistical software. However, the calculations are relatively easy, and are given here for anyone who is interested. The calculations are based on the statistics shown in Table 3. $M_x$ is the mean of $X$, $M_y$ is the mean of $Y$, $S_x$ is the standard deviation of $X$, $S_y$ is the standard deviation of $Y$, and $r$ is the correlation between $X$ and $Y$.
# 
# ### Formulae for standard deviations and correlation
# 
# $$ S_x = \frac{1}{N} \sum (x-\bar{x})^2 $$
# 
# $$ S_y = \frac{1}{N} \sum (y-\bar{y})^2 $$
# 
# $$ R = \frac{1}{S_x S_y} \sum (x-\bar{x})(y - \bar{y}) $$

# <codecell>

Mx = mean(x)
My = mean(y)
Sx = std(x,ddof=1) # note the ddof=1 which means N-1 
Sy = std(y,ddof=1)
Sxy = corrcoef(x,y)
R = Sxy[0,1] # off-diagonal is the correlation coefficient
print '%4.3f %4.3f %4.3f %4.3f %4.3f' % (Mx,My,Sx,Sy,R)

# <markdowncell>

# $$ b = R \; Sy/Sx $$
# $$ a = \bar{y} - b \bar{x} $$

# <codecell>

b = R*Sy/Sx; print 'b = %4.3f' % b
a = My - b*Mx; print 'a = %4.3f'% a

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
    # print "y=ax+b"
    # print "N= %d" % N
    # print "a= %g \\pm t_{%d;\\alpha/2} %g" % (a, N-2, sqrt(Var_a))
    # print "b= %g \\pm t_{%d;\\alpha/2} %g" % (b, N-2, sqrt(Var_b))
    # print "R^2= %g" % RR
    # print "s^2= %g" % ss
    return a, b, RR

# <codecell>

a,b, RR = linreg(x,y)
print a, b

# <markdowncell>

# ### Standardized Variables
# 
# The regression equation is simpler if variables are **standardized** so that their means are equal to 0 and standard deviations are equal to 1, for then $b = r$ and $a = 0$. This makes the regression line:
# 
# $$ Z_y = (R)(Z_x) $$
# 
# where $Z_y = y - \bar{y}$, $Z_x = x - \bar{x}$, $R$ is the correlation, Note that the slope of the regression equation for standardized variables is $R$.

# <codecell>

figure(figsize=(10,8))
plot(x,y,'o',markersize=8)
xlim([0.0, 6.0])
ylim([0.0, 4.0])
xlabel('$x$',fontsize=16)
ylabel('$y$',fontsize=16)
plot(x,ytag,'-',lw=2)
legend((r'$y$',r"$y'$"),fontsize=16)

# <codecell>


