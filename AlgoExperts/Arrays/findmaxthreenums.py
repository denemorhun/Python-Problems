# EASY
''' 

find max three numbers from an array without initializing a new array

O(n)
s(1)

'''

def findmaxthreenums(arr):

    # array to store the largest three values
    threeLargest = [None, None, None]

    for num in arr:
        updateLargest(threeLargest, num)

    return threeLargest

# check if number is none or larger than our current number
def updateLargest(threeLargest, num):
    #compare the current number to the third value, which is max
    if  threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2 ) #TODO
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

# idx is the greatest index in our max list to be updated to minimize shifts
def shiftAndUpdate(threeLargest, num,  idx):
    for i in range(idx + 1):
        # if we are at the last idx assign number
        if i == idx:
            threeLargest[i] = num
        # shift array 
        else:
            threeLargest[i] = threeLargest[i+1]

    
            



    



	

if __name__ == '__main__':
        input = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        input2 = [0, 1, 21, 45, 41, 61, 33, 71, 99, 73]
        input3 = [9]
        input4 = [6, 2, 5, 9, 8, 3]

        result = findmaxthreenums(input4)

        print(result)

