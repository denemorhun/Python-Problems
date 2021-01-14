#!/bin/python3
# implementation of bubblesort using counting number of swaps
# if number of swaps is zero, the array is sorted

def bubblesort(a):
    if len(a) == 0:
        return None
        
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
               

a = [99, 73, 71, 61, 45, 45, 41, 33, 21, 1, 0]


bubblesort(a)