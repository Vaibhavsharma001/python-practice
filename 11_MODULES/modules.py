# Python Modules

# math module
import math

print(math.sqrt(25))
print(math.pi)

# import only one function
from math import factorial

print(factorial(5))

# alias
import math as m

print(m.floor(5.8))

# random module
import random

print(random.randint(1, 10))

# datetime module
import datetime

print(datetime.datetime.now())

# os module
import os

print(os.getcwd())

# statistics module
import statistics

marks = [50, 60, 70, 80, 90]

print(statistics.mean(marks))
print(statistics.median(marks))

print("Program Ended")