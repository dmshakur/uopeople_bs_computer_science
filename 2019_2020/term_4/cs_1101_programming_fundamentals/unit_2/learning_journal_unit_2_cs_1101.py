import math
from random import random
import numpy as np

def print_volume(r):
    return (4 / 3) * (math.pi * r * 3)

print_volume(4.1)

print_volume(2.2)

print_volume(9)

#   #   #   #   #   #   #   #   #   #   #

def dot_product(vec_1, vec_2):
    if (len(vec_1) is not len(vec_2)):
        return "Invalid arguments, pass in 2 lists, tuples or other iterable type"
    return_val = 0
    for i in range(len(vec_1)):
        return_val += vec_1[i] * vec_2[i]
    return return_val

def create_list(num):
    return [random() for i in range(num)]

print('dot_product dot:', dot_product(create_list(4), create_list(4)))

print('dot_product dot:', dot_product(create_list(7), create_list(9)))

print('dot_product dot:', dot_product("string theory", "cats eating cat food"))
