#!/bin/python3

import sys

def bubblesort(n, a):
    if n == 0:
        return 0
    
    size = len(a) - 1
    number_of_swaps = 0
    
    for i in range(size):
        curr_no_swaps = 0
        print("i", i)
        for j in range (size):
            print("j", j)
            if a[j] > a [j+1]:
                print ("a[j], a[j+1]", a[j], a[j+1])
                a[j], a[j+1] = a[j+1], a[j]
                print ("a[j], a[j+1]", a[j], a[j+1])
                curr_no_swaps += 1
        if curr_no_swaps == 0:
            break
        else:
            number_of_swaps += curr_no_swaps
            
    print(f"Array is sorted in {number_of_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[size]}")
    print(a)
               

                
            
                
# the size of the array
n = int(input().strip())
# array, split by " "
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

bubblesort(n, a)