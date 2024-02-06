#
# if data is not suitable for linear regression analysis (i.e., r value comes out close to 0)
# then it may be suitable for polynomical regression analysis
#

import numpy
import matplotlib.pyplot as pyplot
from scipy import stats
from sklearn.metrics import r2_score

xdata = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
ydata = [100, 90, 80, 60, 60, 55, 60, 65,
         70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# first, let's try linear analysis and see what our r says
# we'll create the line of best fit and draw it to illustrate the difference between linear & polynomial fits for this data set
slope, intercept, r, p, std_err = stats.linregress(xdata, ydata)


def linear_regression_pred(x):
    return slope * x + intercept


line_of_linear_regression = list(map(linear_regression_pred, xdata))

print("r value when attempting linear regression analysis is {}".format(r))

polynomial_degree = 3
poly_model = numpy.poly1d(numpy.polyfit(xdata, ydata, polynomial_degree))

# the third argument is the number of data points which will be generated
poly_line = numpy.linspace(min(xdata), max(xdata), 100)

# similar to the linear analysis r value, we can calculate an "r-squared" value for our polynomial regression analysis
# between 0 & 1, 1 from no-correlation to complete-correlation
print("r-squared value when attempting polynomial regression analysis of degree {} is {}".format(
    polynomial_degree, r2_score(ydata, poly_model(xdata))))

# we can see the r-squared value with a degree-3 polynomial regression is high (0.94) we can use the poly_model model to
# predict the y value for any x value
print("our model predicts a y value for an x of 17 to be {}".format(poly_model(17)))

pyplot.scatter(xdata, ydata)
pyplot.plot(xdata, line_of_linear_regression)
pyplot.plot(poly_line, poly_model(poly_line))
pyplot.show()
