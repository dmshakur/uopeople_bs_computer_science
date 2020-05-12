
# Learning Journal Unit 4 CS 1101

# Creating a function called stats that expects a list and returns an dictionary
# The dictionary will contain various numerical values pertaining to certain statistical equations, such as kurtosis and standard deviation

# Refactored a lot of the code for readability and efficiency, for example combining all for loops into one
# Changed std_dev to variance in if, elif statement followint for i in range(int(n)) loop, the first step in the variation equation is the same as the first step in the standard variation equation

# Importing Number to check for numerical values in the input argument
from numbers import Number
# Imported sqrt from math to calculate the standard deviation for the list provided
from math import sqrt

# First step is creating the function, and if statements to ensure that it is passed proper input
def stats(input, population_or_sample):

    if (population_or_sample != 'population') and (population_or_sample != 'sample'):
        print('You must determine if you are inputing a sample or a population of data.')
        return
# Changed the elif statement to check if input is a list of numerical values
    for i in range(len(input)):
        if not isinstance(input[i], Number):
            print('You must send in a list or other iterable type as an argument. You included type: ' + str(type(input)))
            return

    stats = {}

# Added calculations for the mean and n
    n = float(len(input))
    mean = sum(input) / n
# Changed the name of samp_std_dev or pop_std_dev in the stats dict to just std_dev for simplicity
    std_dev = 0.
    variance = 0.
    skewness = 0.
    kurtosis = 0.
    std_err = 0.
    z_scores = []

# Implemented code for variance, standard deviation, skewness and kurtosis.
    for i in range(int(n)):
        variance += (input[i] - mean)**2
        skewness += (input[i] - mean)**3
        kurtosis += (input[i] - mean)**4

    if population_or_sample == "sample":
        std_dev = sqrt(variance / (n - 1.))
        variance /= n - 1
    elif population_or_sample == "population":
        std_dev = sqrt(variance / n)
        variance /= n

# Implemented z scores
    for i in range(int(n)):
        z_scores.append((input[i] - mean) / std_dev)

# Added standard error
    std_err = std_dev / sqrt(n)
    skewness = (skewness / (std_err**3)) / n
    kurtosis = (kurtosis / (std_err**4)) / n

# Adding all stat values to the stats dictionary
    stats['mean'] = mean
    stats['std_dev'] = std_dev
    stats['variance'] = variance
    stats['skewness'] = skewness
    stats['kurtosis'] = kurtosis
    stats['z_scores'] = z_scores
    stats['std_err'] = std_err

    return stats

# Testing

from random import random

sample_data = [ i * random() for i in range(50)]
pop_data = [i * random() for i in range(100)]
more_sample_data = [i for i in range(20)]

sample_data_stats = stats(sample_data, population_or_sample = 'sample')
pop_data_stats = stats(pop_data, population_or_sample = 'population')
more_sample_data_stats = stats(more_sample_data, population_or_sample = 'sample')

print(pop_data_stats)
print(sample_data_stats)
print(more_sample_data_stats)
