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

    chain1 = [i for i in range(21)]
    chain2 = [1,0,3,2,5,4,7,6,9,8,11,10,13,12,15,14,17,16,19,18,20]

    print 'Chain 1 is:'
    print(chain1)

    print 'Chain 2 is:'
    print(chain2)

    crosses = crossover(chain1, chain2, 5)

    print 'Chain 3 is:'
    print(crosses[0])

    print 'Chain 4 is:'
    print(crosses[1])

    return

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
