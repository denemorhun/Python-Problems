# Cracking the coding inverview Book #

''' Find the number of pairs from an array that their difference is k 

 use a dictionary with the pairs of x, x + k
'''



def find_diff_pairs_naive(arr, k):

    count = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if abs (arr[i] - arr[j]) == k:
                print((arr[i], arr[j]))
                count += 1

    return count


def find_diff_pairs(arr, k):

    count = 0
    # use hash table 

    dict = {}
    # loop through array and assign value with a complimentary value in dict
    for item in arr:
        dict[item]  = item + k # O(n)

    for key, value in dict.items():
        if value in arr: # O(n))
            print(key, value)
            count += 1

    return count 

# test
arr1 = [1, 3, 5, 6, 8, 1000]

#print(find_diff_pairs_naive(arr1, 2))
print(find_diff_pairs(arr1, 2))



# how to make it more efficient using hashtable:

