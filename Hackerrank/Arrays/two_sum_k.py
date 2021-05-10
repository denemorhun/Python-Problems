# 2 sum in an array

'''
Calculate the number of pairs that sum up to a value, 
return indices
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

def two_sum(a, k):

    output = []

    # Not enough characters in the array
    if len(a) == 1 or len(a) == 0:
        return None

    # initialize dictionary
    comp_nums = {}

    for i in range(len(a)):
        # if potential match = k - a[i] is already in keys, add indices of value and comp value as tuple
        if k - a[i] in comp_nums.keys():
            output.append((comp_nums[k-a[i]], i))
        else:
            # if potential match doesn't exist, initialize with current index
            comp_nums[a[i]] = i

    # # returning the number instead
    # for n in a:
    #     # potential match = k - n
    #     if k - n in comp_nums:
    #         output.append((k - n , n))
    #     else:
    #         comp_nums[n] = n

    return output
     

if __name__ == '__main__':

    ar = [9, 10, 10, 10, 20, 20, 30, 50, 50, 50] # 3 pairs
    ar2 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2] # 5 pairs
    ar3 = [1, 2, 2, 2, 2, 3,3,3,3,3] # 0 pairs
    ar4 = [1,2,4,5,6,8, 10,13,18]

    result = two_sum((ar4),16)

    print ('indices are {} '.format(result))