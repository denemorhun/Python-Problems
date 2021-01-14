# EASY
'''
Binary search array, target recursively
'''

def insertionsort(array):

    # compare i with i + 1
	# count number of swaps 
	# if we have 0 swaps, its sorted
	# we need to start at x + 1 node each time.
	
    size = len(array) - 1

    # traverse array starting second index
    for i in range(1, size):
        for j in range(0, i):
            if array[i] < array [j]:
                print(f"Swapping {array[i]}, {array[j]} ")
                array[i], array[j] = array[j], array[i]
                print(array)
        
    # array has been sorted
    return array   

if __name__ == '__main__':
        input = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        input2 = [0, 1, 21, 45, 41, 61, 33, 71, 99, 73]
        input3 = [9]
        input4 = [2, 5, 5, 6, 8, 9, 3]

        result = insertionsort(input4)

        print(result)
        
        
