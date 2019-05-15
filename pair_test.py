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

    city_count = 20
    chains = list()
    selections = 10

    c1 = [i for i in range(city_count)]
    c2 = c1[::-1]
    c3 = [1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18]
    c4 = c3[::-1]

    genomes = [c1, c2, c3, c4]

    print 'These are the genomes'
    for i in range(len(genomes)):
        print(genomes[i])

    pairs = pair(genomes, 'ruthless')

    print 'These are the pairs:'
    print(pairs[0])

    print 'And:'
    print(pairs[1])

    return

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
