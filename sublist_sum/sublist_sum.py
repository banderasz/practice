"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
"""
from itertools import combinations
lst = [9, 1, 3, 8]
k = 17

def two_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == k:
                return True
    return False


def two_sum_version2(lst, k):
    lst.sort()
    for element in lst:
        if (k-element) in lst:
            return True
    return False


def any_sum(lst, k):
    for i in range(1, len(lst)+1):
        for comb in combinations(lst, i):
            if sum(comb) == k:
                return comb
    return False
print(two_sum_version2(lst, k))