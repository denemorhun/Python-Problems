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

    for i in range(size):
         # if array is already sorted, the swap count is 0
        swaps = 0
        for j in range(size-i):
            if array[j] > array [j + 1]:
                print(f"Swapping {array[j]}, {array[j+1]} ")
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
                print("Num of swaps:", swaps)
                print(array)

        # must iterate and check for swaps at each iteration.
        # if swaps are reached 0, terminate early
        if swaps == 0:
            print("Reached 0 swaps, breaking")
            break

           
    return array   

if __name__ == '__main__':
        input = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        input2 = [0, 1, 21, 45, 45, 41, 61, 33, 71, 99, 73]
        input3 = [9]

        result = bubbleSort(input2)

        print(result)
        
        
