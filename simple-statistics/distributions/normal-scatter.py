#
# creation of a scatter plot using numpy's distribution data
#

import numpy
import matplotlib.pyplot as pyplot

xdata = numpy.random.normal(1.0, 5.0, 1000)
ydata = numpy.random.normal(3.0, 10.0, 1000)

# note that the method also accepts numpy's ndarray class as args
pyplot.scatter(xdata, ydata)
pyplot.show()