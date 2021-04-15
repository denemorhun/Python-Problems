'''
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the third index will have second-largest, and so on. In other words, all the odd-numbered indices will have the largest numbers in the list in descending order and the even-numbered indices will have the smallest numbers in ascending order.

Input: #
A sorted list

Output: #
A list with elements stored in max/min form

Sample Input #
lst = [1,2,3,4,5]
Sample Output #
lst = [5,1,4,2,3]
'''
from collections import deque

def max_min(a):
    
    out = []

    a = deque(sorted(a)) # O(n*log(n)) s(n)

    print(a)

    while len(a) != 0:
        if len(a) != 0:
            out.append(a.pop())
        if len(a) != 0:
            out.append(a.popleft())

    return out

max_min([1, 2, 3, 4, 5])


# O(n) solution

def max_min_opt(a):
    result = []
    # iterate half list
    for i in range(len(a)//2):
        # Append corresponding last element
        result.append(a[-(i+1)])
        # append current element
        result.append(a[i])
    if len(a) % 2 == 1:
        # if middle value then append
        result.append(a[len(a)//2])
    return result