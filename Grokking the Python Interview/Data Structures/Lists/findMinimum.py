''' 
find the minimum in an array 

# compare the min value with every other value, update min

'''
import heapq as q

# O (n ) solution
def findMinimum(a):
    s = len(a)
    min = a[0]

    for elem in a:
        if elem < min:
            min = elem

    return min

assert 2, findMinimum([9, 2, 3, 6])
assert 1, findMinimum([4, 2, 5, 1])
assert -5, findMinimum([4, 2, -1, -5, 0])
assert 1, findMinimum([1, 1, 1, 1])


def findMinimumHeap(a):

    return q.nsmallest(a)

assert 1, findMinimumHeap([4, 2, 1, 5])

