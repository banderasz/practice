"""Given K sorted lists of integers, return the smallest interval (inclusive) that contains at least one element from
each list. If there are multiple intervals of the same size, return the one that starts at the smallest number. """

test = [[0, 1, 4, 17, 20, 25, 31], [5, 6, 10], [0, 3, 7, 8, 12]]

check = list()

for lst in test:
    check.append(lst.pop(0))

mina = min(check)
minb = max(check)
do = True
while do:
    a = min(check)
    b = max(check)
    if (b-a) < (minb-mina):
        mina = a
        minb = b
    minindex = 0
    for i in range(len(check)):
        if check[i] is not None:
            if check[i] == a:
                minindex = i
    if test[minindex]:
        check[minindex] = test[minindex].pop(0)
    for lst in test:
        if not lst:
            do = False


print(mina, minb)
