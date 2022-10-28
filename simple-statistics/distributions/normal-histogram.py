#
# creation of normal-distributed data and basic visualisation
#

import numpy
import matplotlib.pyplot as pyplot

# see https://numpy.org/doc/1.16/reference/routines.random.html#distributions for numpy's available distributions
# e.g., create 100,000 values using the 5, 1 normal distribution - mean 5, std dev 1
distdata = numpy.random.normal(5.0, 1.0, 100000)

# the random distribution functions return an ndarray object, a wrapper from the
# numpy module with extra info about the generated dataset

# mathplotlib is a library for creating visualisations
# here we create a simple histogram to show our data 
pyplot.hist(distdata)
pyplot.show()