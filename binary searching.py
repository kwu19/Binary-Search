#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:16:19 2018

@author: kefei
"""

def binary_search(arr, elem, start=0, end=None):
    """Binary search without list slicing
    
    Take parameter an array and the element we want to find
    start and end is initially set so no need to input"""
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return True
    if elem < arr[mid]:
        return binary_search(arr, elem, start, mid-1)  # do the recusion without list slicing
    else:
        return binary_search(arr, elem, mid+1, end)
    

# Simple test. Do more below...
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))

from random import sample, choices
import matplotlib.pyplot as plt
import numpy as np
import timeit
import random

big_list_1 = choices(range(100_000), k=100)
big_list_2 = choices(range(100_000), k=200)
big_list_3 = choices(range(100_000), k=500)
big_list_4 = choices(range(100_000), k=1_000)
big_list_5 = choices(range(100_000), k=1_250)
big_list_6 = choices(range(100_000), k=2_000)
big_list_7 = choices(range(100_000), k=2_500)
big_list_8 = choices(range(100_000), k=3_000)
big_list_9 = choices(range(100_000), k=5_000)
big_list_10 = choices(range(100_000), k=10_000)
big_list_11 = choices(range(100_000), k=20_000)

big_lists = [big_list_1, big_list_2, big_list_3, big_list_4, 
             big_list_5, big_list_6, big_list_7, big_list_8, 
             big_list_9, big_list_10, big_list_11]

results = []
for lst in big_lists:
    t = timeit.Timer("binary_search(alist, item)", globals={"binary_search":binary_search,
                                                            "alist":lst, "item":100_000_000})
    results.append(t.timeit(10))
print(results)

sizes = [len(lst) for lst in big_lists]

fig, ax = plt.subplots()
plt.ylabel("Running Time (ms)")
plt.xlabel("Input Size ($N$)")
ax.plot(sizes, results, 'o', label='Binary Search', color='b')

legend = plt.legend(loc='center right', fontsize='small')
plt.show()  # By the plot, we can see that the timing is really similar to $O(log_2(n))$

