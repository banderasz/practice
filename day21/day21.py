"""Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum
number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

array = [(1, 8), (2, 5), (5, 6), (3, 7)]

sorted_array = sorted_colors = sorted(array, key=lambda x: x[0])

num_of_rooms = 1
i = 0
while True:
    if len(sorted_array) <= i + num_of_rooms:
        break
    else:
        if sorted_array[i][1] > sorted_array[i + num_of_rooms][0]:
            num_of_rooms += 1
        else:
            i += 1

print(num_of_rooms)
