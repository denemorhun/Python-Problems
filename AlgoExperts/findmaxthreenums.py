# EASY
''' 

find max three numbers from an array without initializing a new array

O(n)
s(1)

'''

def findmaxthreenums(arr):

    size = len(arr)

    if size < 3:
        return arr

    max_3_items = []

    
    # traverse array, assume first entry in unsorted array is max
    for i in range(1, size):
        curr_max = arr[i-1]
        
        # find the second max value in the remainder array
        if arr[i] > curr_max:
            curr_max = arr[i]

            max_3_items.append(curr_max)

    print("Final max", (curr_max)

    # array has been sorted
    return max_3_items   

if __name__ == '__main__':
        input = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        input2 = [0, 1, 21, 45, 41, 61, 33, 71, 99, 73]
        input3 = [9]
        input4 = [6, 2, 5, 9, 8, 3]

        result = findmaxthreenums(input2)

        print(result)
        
        
