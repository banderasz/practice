"""

Given an array of integers, return a new array such that each element at index i of the new array is the product of
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].
"""
import functools
import itertools
X = [1, 2, 3, 4, 5]

def array_product(X):
    total = functools.reduce(lambda x,y: x*y, X)
    return [int(total/x) for x in X]

def array_product_2(X):
    out = []
    for i in range(len(X)):
        out.append(functools.reduce(lambda x,y: x*y, [*X[:i], *X[i+1:]]))
    return out

print(array_product_2(X))