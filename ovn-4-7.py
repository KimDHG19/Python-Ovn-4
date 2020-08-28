# 7
from tabulate import tabulate
from math import sqrt

i = 1

result = []

for i in range(0, 21):
    result.append([i, sqrt(i), i ** (1. / 3.)])

print(tabulate(result, headers=['i', 'sqrt of i', 'cube of i']))

