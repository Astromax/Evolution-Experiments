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

    chain1 = [1,2,3,4,5,6,7,8,9,0]
    chain2 = [1,4,3,2,5,7,6,9]

    print 'Chain 1 is:'
    print(chain1)

    print 'Chain 2 is:'
    print(chain2)

    e_distance = edit_distance(chain1, chain2)

    print 'The edit distance between chain1 and chain2 is %d' % e_distance

    return

#------------------------------------------------------------------------------
def edit_distance(chain1, chain2):

    distance = 0

    oneago = None
    thisrow = range(1, len(chain2) + 1) + [0]
    for x in xrange(len(chain1)):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(chain2) + [x + 1]
        for y in xrange(len(chain2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (chain1[x] != chain2[y])
            thisrow[y] = min(delcost, addcost, subcost)
    distance = thisrow[len(chain2) - 1]

    return distance
#------------------------------------------------------------------------------                                                                                 
if __name__ == '__main__': main()

# EOF
