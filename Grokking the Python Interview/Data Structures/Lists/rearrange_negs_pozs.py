''' 

Implement a function rearrange(lst) which rearranges the elements 
such that all the negative elements appear on the left and 
positive elements appear at the right of the list. Note that 
it is not necessary to maintain the sorted order of the input list.

Generally zero is NOT positive or negative, we will treat 
zero as a positive integer for this challenge! So, zero will be placed at the right.

MUST DO THIS WITHOUT USING AXULLIARY (i.e. new) Arrays. 

Hint: iterate over the entire list and, if we encounter a negative element, 
we simply swap it with the leftmost positive element since order is unimportant. 
'''

def rearrange(a):
    leftmost_positive_idx = 0

    for i in range(len(a)):
        if a[i] < 0:
            # swap with the leftmost positive element
            a[leftmost_positive_idx], a[i] = a[i], a[leftmost_positive_idx]
            # increment the leftmost index when we do a swap
            leftmost_positive_idx += 1

    print(a)

rearrange([-8, 5, -4, 8, 0, -7, 1])
rearrange([-1, 2, -3, -4, 5])
rearrange([300, -1, 3, 0])
        

