#
# examples of basic stats functions in the numpy & scipy modules
#

import numpy
import random
from scipy import stats

# use random's sample function to generate a list of numbers
data = random.sample(range(1, 100), 20)

# numpy gives us basic stat methods
mean = numpy.mean(data)
median = numpy.median(data)

# mode() function returns a ModeResult object w/ modes and counts
mode = stats.mode(data)

print("mean: {}, median: {}, mode: {}".format(mean, median, mode))

# numpy can also give us the standard deviation & variance
stddev = numpy.std(data)
var = numpy.var(data)

# remember std dev is sqrt(var), and tells us how far on average the values are from the mean
print("standard deviation: {}, variance: {}".format(stddev, var))

# we can easily get percentiles - what value is x% of the data less than
print("25. percentile: {}, 75. percentile: {}".format(numpy.percentile(data, 25), numpy.percentile(data, 75)))