# Remove Dupes from sorted array

'''
Method 1: Return length of array without dupes

Given a sorted array nums, remove the duplicates in-place, each element shoould appear only once 
return the new length.

*** Do not allocate extra space for another array, solve with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5.

Approach:

    # first pointer to point the position which element is being stored to
    # second pointer to iterate the elements. 
    # If the current element and the previous element are different, 
    # store the current element in the first pointer and move one. 
    # Make exception for the first element and in case element is only 0 or 1 size.

    [1, 1, 3, 4, 4, 5, 6, 6] -> [1, 3, 4, 5, 6, 5, 6, 6]

    '''

# complexity of O(1) to calculat length
def length_no_dupes(nums):
   
    if len(nums) == 0:
        return 

    i = 0
    count = 1

    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            count += 1
        i +=1 

    return count 

# Two pointer method to calculate redux array and size
def remove_dupes(nums):

    nums = sorted(nums)

    if len(nums) == 0:
        return None

    size = len(nums)

    # use j to traverse the array

    # use i to keep track of the left array with distinct values
    i = 0

    for j in range(1, size-1):
        # increment i only if values differ
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        # else if values are equal, traverse array using j 

    # print the array redux 
    len_redux = i + 1
    x = 0
    while x <= len_redux:
        print("values", nums[x])
        x += 1

    print("The length of array", len_redux)


if __name__ == '__main__':

    ar = [9, 10, 10, 10, 20, 20, 30, 50, 50, 50] # 3 pairs
    ar2 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2] # 5 pairs
    ar3 = [1, 2, 2, 2, 2, 3,3,3,3,3] # 0 pairs

    print (f'Length of array without dupes {length_no_dupes(ar)}')

    remove_dupes(ar)