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

    new_chains = pseudoclones(chain)
    print 'The new chains are: '
    for c in range(len(new_chains)):
        print(new_chains[c])
    
    return
#------------------------------------------------------------------------------
def pseudoclones(chain):

    N = len(chain)
    new_chains = [[] for i in range(N)]
    for i in range(N-1):
        new_chains[i] = chain[:]
        new_chains[i][i+1], new_chains[i][i] = new_chains[i][i], new_chains[i][i+1]

    return new_chains

#------------------------------------------------------------------------------                                                                                       
def mutation(chain, mode, n):

    N = len(chain)

    print 'The length of the chain is %i' % N

    new_chains = [[] for i in range(n)]
    if mode=='adjacent_swap':
        for i in range(n):
            r1 = random.randint(1, N-2)
            new_chains[i] = chain[:]
            new_chains[i][r1+1], new_chains[i][r1] = new_chains[i][r1], new_chains[i][r1+1]
    elif mode=='random_swap':
        for i in range(n):
            r1 = random.randint(1, N-1)
            r2 = random.randint(1, N-1)
            new_chains[i] = chain[:]
            new_chains[i][r2], new_chains[i][r1] = new_chains[i][r1], new_chains[i][r2]
    elif mode=='self_cross':
        for i in range(n):
            xpoint = random.randint(1, N-1)
            subchain = chain[:xpoint]
            counterchain = chain[xpoint+1:]
            new_chains[i] = counterchain + subchain
    elif mode=='multi_random':
        MR = N/10
        print 'The mutation rate is %i' % MR
        for i in range(n):
            new_chains[i] = chain[:]
            for j in range(MR):
                r1 = random.randint(1, N-1)
                r2 = random.randint(1, N-1)
                new_chains[i][r2], new_chains[i][r1] = new_chains[i][r1], new_chains[i][r2]


    return new_chains

#------------------------------------------------------------------------------                                                                          
if __name__ == '__main__': main()

# EOF
