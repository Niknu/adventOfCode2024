#!/usr/bin/env python 3
import numpy as np
from collections import Counter

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


    right_counter = Counter(right)
    
    similarity_score = sum(value * right_counter[value] for value in left)
    
    print(similarity_score)
