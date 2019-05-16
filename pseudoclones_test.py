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

    chain = [i for i in range(20)]
    print 'The first chain is: '
    print(chain)

    new_chain = pseudoclone(chain)
    print 'The new chain is: '
    print(new_chain)
    
    return
#------------------------------------------------------------------------------
def pseudoclone(chain, cities):
    distance = evaluate(chain, cities)
    pseudoclone = chain
    
    N = len(chain)
    new_chains = [[] for i in range(N)]
    for i in range(N-1):
        new_chains[i] = chain[:]
        new_chains[i][i+1], new_chains[i][i] = new_chains[i][i], new_chains[i][i+1]

    for n in new_chains:
        pcdistance = evaluate(n, cities)
        if pcdistance < distance:
            pseudoclone = n
            distance = pcdistance
        
    return pseudoclone
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
