import numpy
import random
from scipy import stats

# use random's sample function to generate a list of numbers
data = random.sample(range(1,100), 20)

# numpy gives us basic stat methods
mean = numpy.mean(data)
median = numpy.median(data)

# mode() fnc returns a ModeResult object w/ modes and counts
mode = stats.mode(data)

print("mean: {}, median: {}, mode: {}".format(mean, median, mode))