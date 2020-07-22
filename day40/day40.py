"""Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
"""
The trick is to XOR them in three base"""
import math


def reverse_three_base(num: int):
    out = list()
    X = int(math.log(num, 3))
    for i in range(X + 1):
        n = num // 3 ** (X - i)
        b = num % 3 ** (X - i)
        out.append(n)
        num = b
    out.reverse()
    return out


def decode_reverse_three_base(array: list):
    num = 0
    for i in range(len(array)):
        num += array[i] * (3 ** i)
    return num


def find_single(array: list):
    out = [0] * int(math.log(max(array), 3) + 1)
    for number in array:
        element = reverse_three_base(number)
        for i in range(len(element)):
            out[i] = (out[i] + element[i]) % 3
    return decode_reverse_three_base(out)


print(find_single([6, 1, 3, 3, 3, 6, 6]))
