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

    naive_genomes = [[] for i in range(city_count)]
    for i in range(city_count):
        naive_genomes[i].append(i)

    for g in naive_genomes:
        used_indices = [g[0]]
        print 'The used index is %i' % used_indices[0]
        for i in range(city_count):
            near_distance = 10000
            for j in range(city_count):
                if j not in used_indices:
                    distance = ( (city_list[j][1] - city_list[g[-1]][1])**2 + (city_list[j][2] - city_list[g[-1]][2])**2 )**0.5
                    if distance < near_distance:
                        close_index = j
                        near_distance = distance
            used_indices.append(close_index)
            g.append(close_index)
            print 'The close index is %i' % close_index


#    naive_optima = open('naive_optima.csv', 'r+')

    with open('naive_optima.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for g in range(city_count):
            score = evaluate(naive_genomes[g], city_list)
            print 'The shortest distance starting in City %i is %f' % (g, score)
            filewriter.writerow(naive_genomes[g])
    #print(genome)

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
if __name__ == '__main__': main()

# EOF
