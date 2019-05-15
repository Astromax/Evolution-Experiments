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

    city_count = 50
    cities = open('cities.txt', 'r+')

    for c in range(city_count):
        c_index = c
        c_xcoor = random.randint(-101,101)
        c_ycoor = random.randint(-101,101)
        cities.write('%i %f %f' % (c_index, c_xcoor, c_ycoor) + '\n')


    return

#------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
if __name__ == '__main__': main()

# EOF