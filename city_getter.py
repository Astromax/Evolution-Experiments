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

    indices = list()
    xcoords = list()
    ycoords = list()

    cities = open('cities.txt', 'r+')
    for line in cities:
        index = line.split(" ")[0]
        xcoor = line.split(" ")[1]
        ycoor = line.split(" ")[2]
        ycoor = ycoor.rstrip()
        indices.append(index)
        xcoords.append(xcoor)
        ycoords.append(ycoor)

    city_list = zip(indices, xcoords, ycoords)

    print 'This is the city list'
    for i in range(len(city_list)):
        print(city_list[i])

    return

#------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
if __name__ == '__main__': main()

# EOF
