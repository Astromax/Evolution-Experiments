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
    population_size = 120

    generation_zero = [[] for i in range(population_size)]

    for j in range(population_size):
        generation_zero[j] = random.sample(range(city_count), city_count)

    print 'There are %i specimens in the zeroth generation' % len(generation_zero)
    print 'Each specimen has %i genes' % len(generation_zero[0])

    print 'The zeroth specimen is:'
    print(generation_zero[0])

    print 'The first specimen is:'
    print(generation_zero[1])

    print '...'
    print 'The last specimen is:'
    print(generation_zero[population_size-1])

    return
#------------------------------------------------------------------------------                                                                                 
if __name__ == '__main__': main()

# EOF
