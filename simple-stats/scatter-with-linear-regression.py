#
# creation of a simple scatter plot with linear regression analysis
#

import matplotlib.pyplot as pyplot
from scipy import stats

xdata = [5, 8, 18, 12]
ydata = [32, 43, 23, 20]

# use scipy stats' linregression function to conduct a linear regression analysis on our data
# r is the coefficient of correlation (-1 to 1, 0 meaning no relationship, 1/-1 meaning 100% correlated)
slope, intercept, r, p, std_err = stats.linregress(xdata, ydata)

# create a list of 'best fit' y values for the x's


def linear_regression_pred(x):
    return slope * x + intercept


line_of_linear_regression = list(map(linear_regression_pred, xdata))

# note that the two array arg must be the same length to avoid a ValueError
pyplot.scatter(xdata, ydata)

# draw the linear regression line
pyplot.plot(xdata, line_of_linear_regression)

pyplot.show()
