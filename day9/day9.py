"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0
or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5. """

def largest_non_adjacent_sum(lst: list):
    sum_lst = [0]
    for i in range(len(lst)):
        if i == 0:
            sum_lst.append(lst[i])
        else:
            sum_lst.append(max(sum_lst[:i]) + lst[i])
    return max(sum_lst)

print(largest_non_adjacent_sum([2, 4, 6, 2, 5]))