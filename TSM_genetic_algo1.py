#!/usr/bin/env python
"""
NAME
    TSM_genetic_algo1.py - Traveling Salesman Problem Genetic Algorithm 1

SYNOPSIS
    The objective here is to solve the Traveling Salesman Problem using a genetic algorithm

DESCRIPTION
    Put description here.

OPTIONS
    -h, --help
        Prints this manual and exits.
        
    -n VAL
        Blah blah.

AUTHOR
    Max Baugh  <mcbaugh@protonmail.com>

TO DO
    - One: generalize the way the hyperparameters are used
    - Two: control the number of offspring per pair/generation
    - Three: apply "group selection" by measuring hyperparameter combo effectiveness

2018-08-09
"""

#------------------------------------------------------------------------------
# imports
#------------------------------------------------------------------------------

## std
import argparse, sys, time, csv
import matplotlib.pyplot as plt
import numpy as np
import random


#------------------------------------------------------------------------------
# globals
#------------------------------------------------------------------------------
timestamp = time.strftime('%Y-%m-%d-%Hh%M')

#------------------------------------------------------------------------------
# options
#------------------------------------------------------------------------------
def options():
    parser = argparse.ArgumentParser()
    return parser.parse_args()

#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
def main():
    ops = options()

    #Hyperparameters
    #pair_mode_probabilities = [0.4, 0.3, 0.3] #Must sum to 1.0
    #mutation_mode_probabilities = [0.25, 0.25, 0.25, 0.25] #Must sum to 1.0
    #mutation_rate = 0.1 #Defines how many swaps happen with multi-random mutation, as a fraction of number of cities
    #initial_population = 1000
    #population_limit = 10000 
    #naive_stack = False #Boolean
    #pseudoclone = False #Decide whether or not applying pseudoclones
    #pseudoclone_generation = 50 #Apply pseudoclones every N generations
    #NoTwins = True #Decide whether or not to apply no-twins
    
    pair_mode = 'egalitarian'
    pair_modes = ['egalitarian', 'random', 'ruthless']
    mutation_modes = ['adjacent_swap', 'random_swap', 'self_cross', 'multi_random']
    population_size = 150
    #limit = 25000
    #selection_size = 2500
    n_generations = 250
    naive_stack = True

    indices = list()
    xcoords = list()
    ycoords = list()

    cts = open('cities.txt', 'r+')
    for line in cts:
        index = int(line.split(" ")[0])
        xcoor = float(line.split(" ")[1])
        ycoor = float(line.split(" ")[2])
        indices.append(index)
        xcoords.append(xcoor)
        ycoords.append(ycoor)

    cities = zip(indices, xcoords, ycoords)
    city_count = len(cities)

    MR = city_count/10
    optima = [0]

    ### Produce the zeroth generation
    generation_zero = [[] for i in range(population_size)]
    for j in range(population_size):
        generation_zero[j] = random.sample(range(city_count), city_count)

    if naive_stack:
        with open('naive_optima.csv', 'r') as csv:
            for row in csv:
                row = row.split(",")
                genome = [int(i) for i in row]
                generation_zero.append(genome)

    past_optima = list()
    generation_count = list()
    generation = generation_zero
    for i in range(n_generations):
        limit = int(len(generation) + 100)
        selection_size = int(len(generation) * 0.25)
#        if i==0:
#            selection_size = 10000
#        else:
#            selection_size = int(len(generation) * 0.25)
        scores = list()
        ### Evaluate and sort the initial population
        for g in generation:
            score = evaluate(g, cities)
            scores.append(score)

        score_set = zip(scores, generation)
        ordered_score_set = sorted(score_set)
        parents = ordered_score_set[:selection_size]
        #Put pseudoclone here
        #Put twin-removal here
        distances = [g[0] for g in parents]
        genomes = [g[1] for g in parents]
        optimal_distance = distances[0]
        past_optima.append(optimal_distance)
        generation_count.append(i)
        if i >= 100 and i % 25 == 0:
            optima.append(optimal_distance)
            if optima[-1] == optima[-2]:
                MR += 1
        if i<(n_generations-1):
            ### Produce the next generation
            mutation_mode = random.choice(mutation_modes)
            generation = next_generation(genomes, pair_mode, mutation_mode, MR, population_size)
            if len(generation) > limit:
                generation = generation[:limit]
            population_size = len(generation)
        if i % 5 == 0:
            print 'The number of individuals in generation %i is %i' % (i, len(generation))
            print 'The optimal distance in generation %i is %f' % (i, optimal_distance)

    print 'The final optimal distance is %f' % optimal_distance
    print 'The optimal genome is: '
    print(genomes[0])

    plt.scatter(generation_count, past_optima)
    plt.xlabel('Generation')
    plt.ylabel('Optimal Distance')
    plt.show()

    return optimal_distance

#------------------------------------------------------------------------------
# free functions
#------------------------------------------------------------------------------
def next_generation(genomes, pair_mode, mutation_mode, MR, population):
    next_gen = list()
    next_gen.append(genomes[0])

    pairs = pair(genomes, pair_mode)
    xpoint = len(genomes[0])/3
    nmutants = (population)/(5*len(pairs))

    for p in pairs:
        new_pairs1 = crossover(p[0], p[1], xpoint)
        new_pairs2 = crossover(p[0][::-1], p[1][::-1], xpoint)
        normals = [p[1], new_pairs1[0], new_pairs1[1], new_pairs2[0], new_pairs2[1]]
        for n in normals:
            next_gen.append(n)
            mutants = mutation(n, mutation_mode, MR, nmutants)
            for m in mutants:
                next_gen.append(m)

#    print 'The number in the next generation is %i' % len(next_gen)

    return next_gen
#------------------------------------------------------------------------------
def evaluate(chain, cities):
    distance = 0

    for i in range(len(chain)-1):
        gene = chain[i]
        subdistance = 0
        try:
            xene = chain[i+1]
            subdistance = ( (cities[xene][1] - cities[gene][1])**2 + (cities[xene][2] - cities[gene][2])**2 )**0.5
        except:
            KeyError
        distance += subdistance

    return distance
#-------------------------------------------------------------------------------
def crossover(chain1, chain2, x):

    set1 = set()
    set2 = set()

    subchain1 = list()
    subchain2 = list()

    for i in range(len(chain1)):
        set1.add(chain1[i]) 
        set2.add(chain2[i])
        subchain1.append(chain1[i])
        subchain2.append(chain2[i])

        if i > x and set1==set2:
            counterchain1 = chain1[i+1:]
            counterchain2 = chain2[i+1:]
            chain3 = subchain2 + counterchain1
            chain4 = subchain1 + counterchain2
            break

    return (chain3, chain4)

#------------------------------------------------------------------------------
def mutation(chain, mutation_mode, MR, n):
    
    N = len(chain)

    new_chains = [[] for i in range(n)]
    if mutation_mode=='adjacent_swap':
        for i in range(n):
            r1 = random.randint(1, N-2)
            new_chains[i] = chain[:]
            new_chains[i][r1+1], new_chains[i][r1] = new_chains[i][r1], new_chains[i][r1+1]
    elif mutation_mode=='random_swap':
        for i in range(n):
            r1 = random.randint(1, N-1)
            r2 = random.randint(1, N-1)
            new_chains[i] = chain[:]
            new_chains[i][r2], new_chains[i][r1] = new_chains[i][r1], new_chains[i][r2]
    elif mutation_mode=='self_cross':
        for i in range(n):
            xpoint = random.randint(1, N-1)
            subchain = chain[:xpoint]
            counterchain = chain[xpoint:]
            new_chains[i] = counterchain + subchain
    elif mutation_mode=='multi_random':
        for i in range(n):
            new_chains[i] = chain[:]
            for j in range(MR):
                r1 = random.randint(1, N-1)
                r2 = random.randint(1, N-1)
                new_chains[i][r2], new_chains[i][r1] = new_chains[i][r1], new_chains[i][r2]

    return new_chains
#------------------------------------------------------------------------------
def pair(genomes, mode):

    N = len(genomes)

    if mode=='random':
        random.shuffle(genomes)
        pairs = zip(*[iter(genomes)]*2)
    elif mode=='egalitarian':
        pairs = list()
        for i in range(N/2):
            pair = (genomes[i], genomes[N-i-1])
            pairs.append(pair)
    elif mode=='ruthless':
        pairs = list()
        for j in range(0, N-1, 2):
            pair = (genomes[j], genomes[j+1])
            pairs.append(pair)

    return pairs

#------------------------------------------------------------------------------
if __name__ == '__main__': main()

# EOF
