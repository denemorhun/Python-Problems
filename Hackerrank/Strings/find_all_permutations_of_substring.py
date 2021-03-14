''' Find all permutations, O(n!), for a string of unique characters such as abcdefgh

-> a

-> ab, ba

-> insert c into all positions

-> merge ( (cab, acb, cab), (cba), (bca), (bac) ) 

Basic approach:

    Base case: Remove characters recursively from input string until last character
        no need to pop anymore

    Else:
        remove 
        x = string.pop()

 '''

from itertools import permutations

# # Maybe this works? 
# def getPermutation1(s, prefix=''):
#         if len(s) == 0:
#                 print(prefix)
#         for i in range(len(s)):
#                 getPermutation(s[0:i] + s[i+1:len(s)], prefix + s[i] )


# getPermutation1('abcde', "")


s = 'ABCD'
p = [''.join(x) for x in permutations(s)]

print(p)
        