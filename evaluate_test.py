#!/usr/bin/env python 

#------------------------------------------------------------------------------                                                                                                 
# imports                                                                                                                                                                               
#------------------------------------------------------------------------------                                                                                                    

## std                                                                                                                                                                                      
import argparse, sys, time
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

#    print 'This is the city list'
#    for i in range(len(city_list)):
#        print(city_list[i])

    generation_zero = [[] for i in range(population_size)]    
    for j in range(population_size):
        generation_zero[j] = random.sample(range(city_count), city_count)

    score_set = list()
    for g in range(len(generation_zero)):
        score = evaluate(generation_zero[g], city_list)
        combo = (score, g)
        score_set.append(combo)

    ordered_score_set = sorted(score_set)

    distances = [i[0] for i in ordered_score_set]
#    print 'The distances are'
#    print(distances)

    print 'The optimal distance is %f' % ordered_score_set[0][0]

    return

#------------------------------------------------------------------------------
def evaluate(chain, cities):
    distance = 0
    print 'This is the current genome'
    print(chain)

    for i in range(len(chain)-1):
        gene = chain[i]
        print 'This is the current gene'
        print(gene)
        print 'Current coordinates: (%f, %f)' % (cities[gene][1], cities[gene][2])
        subdistance = 0
        try:
            xene = chain[i+1]
            #print 'Destination coordinates: (%i, %i)' % (cities[xene][0], cities[xene][1])
            subdistance = ( (cities[xene][1] - cities[gene][1])**2 + (cities[xene][2] - cities[gene][2])**2 )**0.5
        except:
            KeyError
#        print 'The subdistance is %f' % subdistance
        distance += subdistance
#    print 'The total distance is %f' % distance

    return distance
#------------------------------------------------------------------------------                                                                                 
if __name__ == '__main__': main()

# EOF
