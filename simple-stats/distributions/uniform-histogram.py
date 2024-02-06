#
# creation of uniform-distributed data and basic visualisation
#

import numpy
import matplotlib.pyplot as pyplot

# see https://numpy.org/doc/1.16/reference/routines.random.html#distributions for numpy's available distributions
# e.g., create 200 values between 0 & 10 using the Uniform Distribution
distdata = numpy.random.uniform(0.0, 10.0, 10000)

# the random distribution functions return an ndarray object, a wrapper from the
# numpy module with extra info about the generated dataset

# mathplotlib is a library for creating visualisations
# here we create a simple histogram to show our data 
pyplot.hist(distdata)
pyplot.show()