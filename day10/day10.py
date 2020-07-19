"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

from time import sleep

def func_after(f, n):
    sleep(n/1000)
    f()

def print_():
    print("done")

func_after(print_, 10000)