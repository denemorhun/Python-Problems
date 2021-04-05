''' Given two sorted lists, merge
 them into one list which should also be sorted '''

# O(n + m) since both lists must be traversed

def merge_lists(lst1, lst2):
    return sorted(lst1 + lst2)

l1 = [1,3,4,5]  
l2 = [2,6,7,8]

print(merge_lists(l1, l2))