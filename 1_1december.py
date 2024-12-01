#!/usr/bin/env python 3
import numpy as np

if __name__ == "__main__":


    # left = np.array( [3,
    #         4,
    #         2,
    #         1,
    #         3,
    #         3,])
    # right = np.array([4,
    #         3,
    #         5,
    #         3,
    #         9,
    #         3,])

    data =  np.loadtxt('input.txt')
    left = data[:,0]
    right = data[:,1]


    print("left before =",left)
    print("right before =",right)
    
    left = np.sort(left)
    right = np.sort(right)
    print("right after =",right)
    print("left after =",left)

    distance = np.array([])
    for (left, right) in zip(left, right):
        
        distance = np.append(distance, abs(left-right))
    
    print(distance.sum())
