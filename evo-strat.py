# Evolutionary Computing A412
# Project 2: Evolution Strategies
# Mar 9, 2018
# Henry Thomas - htthomas@alaska.edu
# Dakota Crowder - dcrowder2@alaska.edu

import math as m
import random as r
import numpy as np
import matplotlib.pyplot as plt

x0 = 0
x1 = 1
sigma0 = 2
sigma1 = 3


def func(X1, x2):
    if -3 <= X1 <= 12 and 4 <= x2 <= 6:
        return 21.5 + (X1 * m.sin(4 * m.pi * X1)) + (x2 * m.sin(20 * m.pi * x2))
    else:
        print "x1 or x2 out of bounds!"


def recombination(mu, count):
    new_mu = []
    rows, cols = np.array(mu).shape
    for not_used in range(count):
        index1 = r.randint(0, rows-1)
        index2 = r.randint(0, rows-1)
        chosen_parent = r.sample([mu[index1], mu[index2]], 1)[0]
        new_parent = [chosen_parent[x0], chosen_parent[x1], np.mean([mu[index1][sigma0], mu[index2][sigma0]]),
                      np.mean([mu[index1][sigma1], mu[index2][sigma1]])]
        new_mu.append(new_parent)
    return new_mu


def reproduce(mu, tau, tau_prime, offspring_count):
    parents = recombination(mu, offspring_count)
    Lambda = np.zeros((offspring_count, 4))
    rows, cols = np.array(parents).shape
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
    rows, cols = np.array(parents).shape
    return [Lambda[int(i[1])] for i in sorted_fitness[:rows]], np.mean(fitness[:, 0]), np.max(fitness[:, 0])


def main():
    offspring_count = input("How many children: ")
    mu_count = input("How many parents: ")
    mu = np.zeros((mu_count, 4))
    for parent in mu:
        parent[x0] = r.uniform(-3, 12)
        parent[x1] = r.uniform(4, 6)
        parent[sigma0] = 1
        parent[sigma1] = 1

    termination_count = input("Termination count: ")
    generations = [0]
    average_fitness = [0]
    best_x12 = [mu[0][x0], mu[0][x1]]
    best_value = [np.max(mu)]
    overall_learning_rate = 1 / m.sqrt(2*termination_count)
    coordinate_learning_rate = 1 / m.sqrt(2*m.sqrt(termination_count))
    for generation in range(termination_count):
        print "Generation " + str(generation)
        generations.append(generation)
        mu, mean_fitness, best = reproduce(mu, overall_learning_rate, coordinate_learning_rate, offspring_count)
        print "Mean fitness: " + str(mean_fitness)
        print "Best fitness: " + str(best)
        if best > np.max(best_value):
            best_x12 = [mu[0][x0], mu[0][x1]]  # The new mu will always have the best fitness as the first object
        average_fitness.append(int(mean_fitness))
        best_value.append(best)
    print "Best Fitness found in generation " + str(np.argmax(best_value)) + " with the fitness value of " \
          + str(np.max(best_value))
    print "With values of\nX0 = " + str(best_x12[0]) + " X1 = " + str(best_x12[1])
    plt.plot(generations, average_fitness, color="blue")
    plt.plot(generations, best_value, color="green")
    plt.xlabel("Generation")
    plt.ylabel("Fitness value")
    plt.title("Fitness Values over the generation\nAverage in blue, best in green")
    plt.show()


if __name__ == "__main__":
    main()
