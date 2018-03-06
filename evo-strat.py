#Evolutionary Computing A412
#Project 2: Evolution Strategies
#Mar 9, 2018
#Henry Thomas - htthomas@alaska.edu
#Dakota Crowder - dcrowder2@alaska.edu

import math as m
import random as r
import numpy as np

x0 = 0
x1 = 1
sigma0 = 2
sigma1 = 3
def func(x1, x2):
    if -3 <= x1 <= 12 and 4 <= x2 <= 6:
        return 21.5 + x1*m.sin(4*m.pi*x1) + x2*m.sin(20*m.pi*x2)
    else:
        print "x1 or x2 out of bounds!"


def reproduce(parents, tau, tau_prime, offspring_count):
    Lambda = np.zeros((offspring_count, 4))
    rows, cols = parents.shape
    for child in Lambda:
        parent = r.randint(0, rows-1)
        child[sigma0] = parents[parent][sigma0] * m.exp((tau_prime * np.random.normal(0, 1)) +
                                                                    (tau * np.random.normal(0, 1)))
        child[sigma1] = parents[parent][sigma1] * m.exp((tau_prime * np.random.normal(0, 1)) +
                                                                    (tau * np.random.normal(0, 1)))
        done = False
        while not done:
            child[x0] = parents[parent][x0] + child[sigma0]*np.random.normal(0, 1)
            if -3 <= child[x0] <= 12:
                done = True
        done = False
        while not done:
            child[x1] = parents[parent][x1] + child[sigma1] * np.random.normal(0, 1)
            if 4 <= child[x1] <= 6:
                done = True
    rows, cols = Lambda.shape
    fitness = np.zeros((rows, 2))
    for index in range(rows):
        fitness[index][0] = func(Lambda[index][x0], Lambda[index][x1])
        fitness[index][1] = index
    sorted_fitness = np.flip(fitness[fitness[:, 0].argsort()], 0)
    rows, cols = parents.shape
    return [Lambda[int(i[1])] for i in sorted_fitness[:rows]]

def main():
    offspring_count = input("How many children: ")
    mu_count = input("How many parents: ")
    mu = np.zeros((mu_count, 4))
    for parent in mu:
        parent[x0] = r.uniform(-3, 12)
        parent[x1] = r.uniform(4, 6)
        parent[sigma0] = 1
        parent[sigma1] = 1

    termination_count = 10000
    
    n = 2 #number of sigmas
    overall_learning_rate = 1 / m.sqrt(2*n)
    coordinate_learning_rate = 1 /  m.sqrt(2*m.sqrt(n))
    print mu
    print reproduce(mu, overall_learning_rate, coordinate_learning_rate, offspring_count)


if __name__ == "__main__":
    main()
