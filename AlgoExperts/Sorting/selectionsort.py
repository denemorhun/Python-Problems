# EASY
'''
selection sort array
Algorithm
repeatedly finding the minimum element (considering ascending order) 
from unsorted part and putting it at the beginning. 
The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element 
(considering ascending order) from the unsorted subarray is
 picked and moved to the sorted subarray.


O(n2)


'''

def selectionsort(arr):

    size = len(arr)

    # traverse array, assume first entry in unsorted array is min
    for i in range(size):
        curr_min = arr[i]
        idx = i
        
        # find the current minimum value in the remainder array
        for j in range(i+1, size):
            if arr[j] < curr_min:
                curr_min = arr[j]
                idx = j

        # swap target min with assumed min
        arr[i], arr[idx] = arr[idx], arr[i]

    # array has been sorted
    return arr   

if __name__ == '__main__':
        input = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        input2 = [0, 1, 21, 45, 41, 61, 33, 71, 99, 73]
        input3 = [9]
        input4 = [6, 2, 5, 9, 8, 3]

        result = selectionsort(input2)

        print(result)
        
        
