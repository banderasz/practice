"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.

Given N, write a function that returns the number of unique ways you can climb the staircase.

Generate the possible ways to go up in N steps with X number of stairs at time.
"""
from collections import defaultdict
from itertools import permutations
from time import time

X = {x for x in range(2,10)}
N = 100


def all_combs(X, N):
    options = set()
    maxstep = N // min(X)
    allist = list()

    def combs(a):
        if len(a) == 0:
            return [[]]
        cs = []
        for c in combs(a[1:]):
            if (len(c)) < maxstep and (sum(c) <= N):
                cs += [c, c + [a[0]]]
        return cs

    for i in range(maxstep):
        for element in X:
            allist.append(element)

    cs = combs(list(allist))

    cs = [list(x) for x in set(tuple(x) for x in cs)]
    for comb in cs:
        if isinstance(comb, list):
            if sum(comb) == N:
                local = tuple([*comb])
                options.add(local)
        else:
            if comb == N:
                options.add(str(comb))
    return options


def one_permutation(X, N, dx=[defaultdict(lambda: set())]):
    d = dx[0]
    for x in X:
        d[x].add((x,))

    d2 = d.copy()
    max_finished = max(d2.keys())

    while True:
        for xi in X:
            for summa in d.keys():
                if summa + max(X) > max_finished:
                    if summa + xi <= N:
                        sub = d2[summa]
                        for element in sub:
                            sub2 = tuple(sorted((*element, xi)))
                            d2[summa + xi].add(sub2)

        stop = True
        for i in range(N + 1):
            if len(d[i]) != len(d2[i]):
                stop = False

        if stop:
            break
        else:
            d = d2.copy()
    dx[0] = d
    return d


def calc_permutations(iter_of_tuple):
    outset = set()
    for i in iter_of_tuple:
        for perm in tuple(permutations(i)):
            outset.add(perm)
    return outset


def use_calced_steps(X, N, dx=[defaultdict(lambda: set())]):
    d = dx[0]
    for x in X:
        d[x].add((x,))

    d2 = d.copy()

    while True:
        for xi in X:
            for summa in d.keys():
                if summa + xi <= N:
                    if d2[summa]:
                        d2[summa + xi].add(tuple(sorted((summa, xi))))

        stop = True
        for i in range(N + 1):
            if len(d[i]) != len(d2[i]):
                stop = False

        if stop:
            break
        else:
            d = d2.copy()
    dx[0] = d
    return d


def calc_known_steps(d, X):
    di = d.copy()
    for key, value in di.items():
        subset = set()
        for option in value:
            for step in option:
                if step == key:
                    subset.add((step,))
                else:
                    suboption = list(option)
                    suboption.remove(step)
                    for option2 in di[step]:
                        if set(suboption).intersection(set(X)) == set(suboption):
                            sub2 = tuple(sorted((*suboption, *option2)))
                            subset.add(sub2)
        di[key] = subset
    return di


def calc_known_steps_recursive(d, X, N):
    di = d.copy()
    subset = set()
    for option in di[N]:
        if set(option).intersection(set(X)) == set(option):
            subset.add(option)
        for step in option:
            if step == N:
                subset.add((N,))
            else:
                suboption = list(option)
                suboption.remove(step)
                for result in calc_known_steps_recursive(di, X, step):
                    if len(result)== 1:
                        if result in X:
                            for element in di[result]:
                                    subset.add((*element, step))
                    else:
                        if set(result).intersection(set(X)) == set(result) and set(suboption).intersection(set(X)) == set(suboption):
                            sub2 = tuple(sorted((*result, *suboption)))
                            subset.add(sub2)

    return subset

#
# d = use_calced_steps(X, 6)
# print(d)
# x = calc_known_steps_recursive(d, X, 6)
# print(x)



start = time()

# for i in range(1,N):
#     d = use_calced_steps(X, i)
#     calc_known_steps(d,X)

d = use_calced_steps(X, N)
print(len(calc_known_steps(d, X)[N]))
print(time() - start)

start = time()

# for i in range(1,N):
#     one_permutation(X, i)

d2 = one_permutation(X, N)
print(len(d2[N]))
print(time() - start)

