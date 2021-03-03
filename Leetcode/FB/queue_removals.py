"""
Queue Removals

https://leetcode.com/discuss/interview-question/1039925/Facebook-Practice-question-or-Queue-Removals


EASY

DS: Q

input arr, x

Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)

Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it

For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then add it back to the queue

Compute a list of x integers output, the ith of which is the 1-based index in the original array of the element which had been removed in step 2 during the ith iteration.

Signature
int[] findPositions(int[] arr, int x)


Return a list of x integers output, as described above.
Example
n = 6
arr = [1, 2, 2, 3, 4, 5]
x = 5
output = [5, 6, 4, 1, 2]
The initial queue is [1, 2, 2, 3, 4, 5] (from front to back).
In the first iteration, the first 5 elements are popped off the queue, leaving just [5]. Of the popped elements, the largest one is the 4, which was at index 5 in the original array. The remaining elements are then decremented and added back onto the queue, whose contents are then [5, 0, 1, 1, 2].
In the second iteration, all 5 elements are popped off the queue. The largest one is the 5, which was at index 6 in the original array. The remaining elements are then decremented (aside from the 0) and added back onto the queue, whose contents are then [0, 0, 0, 1].
In the third iteration, all 4 elements are popped off the queue. The largest one is the 1, which had the initial value of 3 at index 4 in the original array. The remaining elements are added back onto the queue, whose contents are then [0, 0, 0].
In the fourth iteration, all 3 elements are popped off the queue. Since they all have an equal value, we remove the one that was popped first, which had the initial value of 1 at index 1 in the original array. The remaining elements are added back onto the queue, whose contents are then [0, 0].
In the final iteration, both elements are popped off the queue. We remove the one that was popped first, which had the initial value of 2 at index 2 in the original array.
"""

from collections import deque

def findPositions(arr, x):
    
    q = deque()

    holder = deque()

    # pop x elements from q
    if x > len(arr):
        s = len(arr)
    else:
        s = x
    for i in range(s):
        holder.append(arr.pop(0))

    print(holder)

    # from the x elements, remove the max
    holder.remove(max(holder))

    print(holder)

    # for remaining popped elements reduce their values by 1 if > 0
    # append values back to the queue

    for item in holder:
        if item > 0:
            arr.append(item-1)

    print('final', arr)



    

if __name__ == "__main__":

    # Must operate LIFO
    arr = [1, 2, 2, 3, 4, 5]
    x = 5

    findPositions(arr, x)