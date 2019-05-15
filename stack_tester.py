#!/usr/bin/env python 

#------------------------------------------------------------------------------                                                                                                 
# imports                                                                                                                                                                               
#------------------------------------------------------------------------------                                                                                                    

## std                                                                                                                                                                                      
import argparse, sys, time, csv
import numpy as np
import random

#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
def main():

    population_size = 10
    
    indices = list()
    xcoords = list()
    ycoords = list()

    cities = open('cities.txt', 'r+')
    for line in cities:
        index = int(line.split(" ")[0])
        xcoor = float(line.split(" ")[1])
        ycoor = float(line.split(" ")[2])
        indices.append(index)
        xcoords.append(xcoor)
        ycoords.append(ycoor)

    city_list = zip(indices, xcoords, ycoords)
    city_count = len(city_list)

    generation_zero = list()
    with open('naive_optima.csv', 'r') as csv:
        for row in csv:
            row = row.split(",")
            genome = [int(i) for i in row]
            generation_zero.append(genome)

    print 'The number of genomes is %i' % len(generation_zero)
    print 'This is the first genome'
    print(generation_zero[0])

    for i in range(len(generation_zero)):
        score = evaluate(generation_zero[i], city_list)
        print 'The score of genome %i is %f' % (i, score)

    crosses = (generation_zero[1], generation_zero[37], 15)

    print 'This is the first cross'
    print(crosses[0])

    return

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
#------------------------------------------------------------------------------
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
if __name__ == '__main__': main()

# EOF
