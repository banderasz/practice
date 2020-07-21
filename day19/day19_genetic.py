"""A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing
cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal. """
from day19_matrix import create_cost_matrix, read_matrix

"""
Try with genetic algorithm for fun
"""
import pandas as pd
import numpy as np
from random import randint, sample
import matplotlib.pyplot as plt

N = 30
k = 5

# create_cost_matrix(N, k, 15, "test")

population = 50
generation = 500
mut_chance = 0.1
fit_rate = 0.2
breed_rate = 0.5





def generate_person(N, k):
    person = np.random.randint(k, size=N)
    while not check_correct(person):
        person = np.random.randint(k, size=N)
    return person

def breed(parent1, parent2):
    which_one = np.random.randint(2, size=N).astype(np.bool)
    out_array = np.choose(which_one, [parent1, parent2])
    while not check_correct(out_array):
        which_one = np.random.randint(2, size=N).astype(np.bool)
        out_array = np.choose(which_one, [parent1, parent2])
    return out_array

def mutation(old:np.array, mut_chance, k):
    new = old.copy()
    new[np.random.rand(*new.shape) < mut_chance] = np.random.randint(0,k)
    while not check_correct(new):
        new = old.copy()
        new[np.random.rand(*new.shape) < mut_chance] = np.random.randint(0, k)
    return new

def check_correct(element):
    for i in range(len(element)-1):
        if element[i] == element[i+1]:
            return False
    else:
        return True

def fitness(matrix, element):
    sum = 0
    for x,y in matrix.iterrows():
        sum += y[element[x]]
    return sum

def iteration(pop_list):
    fit_vals = [fitness(matrix, x) for x in pop_list]
    print(fit_vals[0])
    sorted_pop_list = [x for _, x in sorted(zip(fit_vals, pop_list), key=lambda pair: pair[0])]
    new_list = sorted_pop_list[:int(fit_rate*population)]
    for _ in range(int(breed_rate*population)):
        kid = breed(*sample(pop_list, 2))
        new_list.append(mutation(kid, mut_chance, k))
    while len(new_list) < population:
        new_list.append(generate_person(N, k))
    return new_list



pop_list = [generate_person(N,k) for _ in range(population)]

matrix = read_matrix("test.xlsx")


best = []
avarage = []
for _ in range(generation):
    pop_list = iteration(pop_list)
    best.append(fitness(matrix, pop_list[0]))
    mean = 0
    for i in range(len(pop_list)):
        mean += fitness(matrix, pop_list[i])/len(pop_list)
    avarage.append(mean)

plt.plot(best, 'b')
plt.plot(avarage, 'r')
plt.show()
print(best[-1])