'''find the min value in a searching window (iterate the start position
 from 0 to the end of the array, the end position relies on the 
 number of swaps left), move it to the head of the current searching '
 window (by swapping it with preceding elements m times), then repeat it 
 in next searching window with k-m swaps.'''
def findMinArray(arr, k):

# index of the current searching window, starts from 0
    cur_ix = 0

# swap counts
    count = 0

# iterate the loop until the array has been swapped k times or cur_ix reaches the end of the array 
# increase cur_ix by 1 in each loop
# in each loop, we find the min value in the searching window of the array, from cux_ix to cur_ix+upper_limit+1
# where upper_limit is the number of swaps left 
# e.g. [8,9,1,11,3,1] k=3, we search [8,9,1,11] first, find min_val=1, move it to the head (needs 2 swaps), 
# so array becomes [1,8,9,11,3,1]
# now we have k-2= 1 swaps left
# then next we search within [8,9], min_val is 8, so we need to swap 0 times
# then we search [9, 11], min_val is 9, swap 0 times
# then search [11,3], min_val is 3, swap 1 times, array becomes [1,8,9,3,11,1], no swaps left, stop
    while count < k and cur_ix < len(arr)-1:
    # update upper_limit to remaining number of swaps 
        upper_limit = min(k-count, len(arr)-1-cur_ix) 

    # find the minimum index from cur_ix to cur_ix+upper_limit+1
    # it's also the number of swaps we can make in the current iteration 
        min_val = min(arr[cur_ix:cur_ix+upper_limit+1])
        min_ix = arr[cur_ix:cur_ix+upper_limit+1].index(min_val)

    # swap the min_val element min_ix times to move it to the head of the searching window  
    # you can write your own swap function to do the min_ix swaps
    # or take out the min_val and insert it to the head directly using python's del() and insert() functions
        temp = arr[cur_ix + min_ix]
        del arr[cur_ix + min_ix]
        arr.insert(cur_ix, temp)
        count += min_ix

        # increase cur_ix by 1
        cur_ix += 1

    return arr