# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:57:50 2017

@author: Tirtha
"""
import random
n = []
swaps =[]
    
def bubble_sort(a):
    
#print (a)    
    flag = True
    swap_count = 0
    while flag:
        flag = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                flag = True
                t = a[i+1]
                a[i+1] = a[i]
                a[i] = t
                swap_count+=1
    return swap_count #Returns the number of swap operations performed
#print (a)
#print ("done")
#print (a)
#print ("It took {} swaps!".format(swap_count))
n_test_case = 200
max_length_array = 1000
for k in range(n_test_case):
    a = []
    Nt = random.randint(0,max_length_array)
    n.append(Nt)
    for i in range(Nt):
        a.append(random.randint(0,100))
    swaps.append(bubble_sort(a))
    
import numpy as np

x = np.array(n)
y = np.array(swaps)

import matplotlib.pyplot as plt

# Plot the # of swap operations performed
plt.scatter(x,y)
plt.title("Number of swaps performed for each bubble sort", fontsize=20)
plt.xlabel("Length of array to be sorted", fontsize=20)
plt.ylabel("Number of swap operation", fontsize=20)
plt.show()
