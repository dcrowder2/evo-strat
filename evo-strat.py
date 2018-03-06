#Evolutionary Computing A412
#Project 2: Evolution Strategies
#Mar 9, 2018
#Henry Thomas - htthomas@alaska.edu
#Dakota Crowder - dcrowder2@alaska.edu

import math as m
import random as r

def func(x1, x2):
    if -3 <= x1 <= 12 and 4 <= x2 <= 6:
        return 21.5 + x1*m.sin(4*m.pi*x1) + x2*m.sin(20*m.pi*x2)
    else:
        print "x1 or x2 out of bounds!"

def main():
    x0 = r.uniform(-3, 12)
    x1 = r.uniform(4, 6)
    number_of_parents = 3
    number_of_offspring = 21
    mutation_step_size = 1
    termination_count = 10000
    
    n = 1 #step_sizes
    overall_learning_rate = 1 / m.sqrt(2*n)
    coordinate_learning_rate = 1 /  m.sqrt(2*m.sqrt(n))
    
    fitness = func(x0, x1)

if __name__ == "__main__":
    main()
