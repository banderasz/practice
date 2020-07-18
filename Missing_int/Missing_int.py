"""Given an array of integers, find the first missing positive integer in linear time and constant space. In other
words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well. """
from typing import Iterable


def find_first_missing(array:Iterable):
    unique = [x for x in set(array) if x > 0]
    for i in range(len(unique)):
        if i+1 !=unique[i]:
            return i+1
    else:
        return len(unique)+1
