''' Kadane's algorithm

# calculate the max_subarray for each index.
    # max_subarray would be either the value at index
    # or max_subarray up till that index + value

'''

from typing import MutableSequence


def kadanesAlgo(a):

    if a is None:
        return None

    # if there is only element, or first, max sub is itself
    ms = a[0]

    output = []

    output.append(ms)

    output_array = []
    

    for i in range(1, len(a)):
        
        
        else:
            i+=1

        output.append(ms)

    print(output)

    #return(output_array)

    return output[-1]
    


# a1 = [-1, 0, 2, -7, 5, 3, 9]
# a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
# kadanesAlgo(a1)

kadanesAlgo([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])
# 3, 3 + 5 > 3, -9+8 > -9, -1+1 < 1, 1+3>1, 4-2 > -2, 2+3 > 2, 4+5 > 4, 9+7> 9
# 16 + 2 > 16, 18-9 > -9, 9+6 > 6, 15+3 > 13, 18+1 > 18, 19-5 > 14, 14+4> 4

'''
a[0] = ms 
if a[i] + ms > ms:
    ms = ms + a[i]
else:
    ms = a[i-1]
'''

assert 19, kadanesAlgo([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])





