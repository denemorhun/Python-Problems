
# EASY

'''
Pair Sums (variation of 2 sum)
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.

If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).

Solution:

'''

#!/bin/python3

from unittest import TestCase

def two_sum_equals_k(arr, k):
    if not arr:
        return 0
    maps = {}

    # number of two sums
    counter = 0

    #traverse the array
    for num in arr:
        print(f'Current number: {num}')

        diff = k - num

        # if number does not exist in the dict, add it's comp
        if num not in maps.keys(): #2
            print(f'comp num {diff} not in dict, add and set to 1 ')
            maps[diff] = 1 #4

         # if comp number is already present a pair must exist
        else:
            print(f'{num} is in dict:')
            
            # num is actually a diff, with a min value of 1

            #4
            counter += maps[num] # inc by 1
            print(f'Inc counter by ', maps[num])
            maps[num] += 1
            print('Increase maps[num] value by 1 to ', maps[num])

    return counter


class TestPairSums(TestCase):
    def setUp(self) -> None:
        self.arr_1 = [1, 2, 3, 4, 3]
        self.arr_2 = [1, 5, 3, 3, 3]
        self.arr_3 = [3, 3, 3, 3, 3, 3]
        self.k = 6

    def test_pair_sums(self) -> None:
        self.assertEqual(2, two_sum_equals_k(self.arr_1, self.k))
        self.assertEqual(4, two_sum_equals_k(self.arr_2, self.k))
        self.assertEqual(1, two_sum_equals_k(self.arr_3, self.k))

 # driver code
    if __name__ == '__main__':
        input = ""

        #l1 = ListNode

        result = two_sum_equals_k([1, 2, 3, 4, 3, 3, 3, 2], 6)

        print('Number of pairs', result)