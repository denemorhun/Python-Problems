# EASY
'''
Insertion sort array
Algorithm
To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, 
compare it to the elements before. 
Move the greater elements one position up to make space for the swapped element.

O(n2)


'''

def insertionsort(array):

    size = len(array)

    # traverse array starting second index
    for i in range(1, size):
        j = i
        while array[j-1] > array [j] and j > 0:
                print(f"swap adjacent elements {array[j]} ")
                array[j-1], array[j] = array[j], array[j-1]
                print(array)
                j-=1
        
    # array has been sorted
    return array   

if __name__ == '__main__':
        input = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        input2 = [0, 1, 21, 45, 41, 61, 33, 71, 99, 73]
        input3 = [9]
        input4 = [6, 2, 5, 9, 8, 3]

        result = insertionsort(input4)

        print(result)
        
        
