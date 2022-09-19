# -*- coding: utf-8 -*-
"""
CSC 212, 222 LAB 3

Created by NAME
14 SEP 2022

Collaborators:
    Isiah
    Demitrius
    Garrett

This program models the growth of the US population from 1790 to the present, 
and it plots the approximation over a plot of the census data. The plot is 
nonlogarithmic. There are five binary operator functions that perform the 
operations +,-,*,/,** respectively. Try to write the code using the fewest 
python defined binary operators, i.e. write your own algorithms for these
basic functions.

Output:

    [Graph]
    
NOTE: Fill in the binOp functions with the correct binary operator and adjust
the code to change the plot from logarithmic to nonlogarithmic. 
    
    Replace NAME after 'Created by' with your name. Replace NAME under 
'Collaborators' with the names of students that helped you or that you helped.
Use docstrings in your functions. Remember to delete 'pass' after you type code
in the functions, the try block, or the except block. DO NOT SUBMIT THE SAME 
CODE AS ANOTHER STUDENT.

"""

import matplotlib.pyplot as plt
import numpy as np

# global variables

CYEARS = [year for year in range(1790,2030,10)]
CENSUS = [3929326,
          5308483,
          7239881,
          9638453,
          12866020,
          17069453,
          23191876,
          31443321,
          39818449,
          50189209,
          62947714,
          76212168,
          92228496,
          106021537,
          122775046,
          132164569,
          150697361,
          179323175,
          203302031,
          226545805,
      	  248709873,
          281421906,
          308745538,
      	  331449281
          ]
GROWTH = [(CENSUS[i+1]-cen)/cen for i,cen in enumerate(CENSUS[:-1]) ]

# functions

def drawUSpop():
    plt.yscale("log")
    plt.plot(CYEARS,CENSUS,'bo')
    plt.xlabel('Years')
    plt.ylabel('Millions')
    plt.title('US Population')
    currentValues = plt.gca().get_yticks()
    trunkValues = largeTickVal(currentValues)
    # plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in trunkValues])

def largeTickVal(tick):
    flags = tick > 1000000
    if True in flags:
        tick = tick/1000000
    return tick

def modelUSpop(t0, tn, P0, kappa):
    time = range(t0,binOpD(tn,1))
    P = [0]*len(time)
    P[0] = P0
    kappa = kappa + [kappa[-1]]
    for i,j in enumerate(time[1:]):
        i = binOpD(i,1)
        k = int(np.floor( binOpE(i,10)))
        P[i] = binOpB(P[binOpC(i,1)], np.exp(binOpE(kappa[k],binOpA(10,1.0497))))
    return time, P


# operators

################################
#
# Finish the following functions
#
################################

def binOpA(val1, val2):
    return val1 + val2

def binOpB(val1, val2):
    return val1 / val2

def binOpC(val1, val2):
    return val1 * val2

def binOpD(val1, val2):
    return val1 + val2

def binOpE(val1, val2):
    return val1 / val2

# main
    
if __name__=='__main__':
      
    try:
        t,P = modelUSpop(CYEARS[0],2022,CENSUS[0],GROWTH)
        drawUSpop()
        plt.plot(t,P)

    except KeyboardInterrupt:
        pass
