# EASY
'''
Binary search array, target recursively
'''

def bubbleSort(array):

    # compare i with i + 1
	# count number of swaps 
	# if we have 0 swaps, its sorted
	# we need to start at x + 1 node each time.
	
    size = len(array) - 1

    i = 0

    # assume if array is already sorted
    swaps = 0



if __name__ == '__main__':
        input = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        input2 = [0, 1, 21, 45, 45, 41, 61, 33, 71, 99, 73]
        input3 = [9]

        result = bubbleSort(input2)

        print(result)
        
        
