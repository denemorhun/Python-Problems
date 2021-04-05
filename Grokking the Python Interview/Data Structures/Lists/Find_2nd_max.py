# find the 2nd max number in an array
# sorting will not work if there are duplicates

def find_2nd_max(a):
    # traverse list and find max m
    max_n = float('-inf')
    max_2 = float('-inf')


    # O(n)
    for num in a:
        if num > max_n:
            max_n = num

    print('max_n', max_n)

    # O(n)
    for num in a:
        if num > max_2 and num != max_n:
            max_2 = num
    
    return max_2

    # traverse list and if value not the max m, return

#print (find_2nd_max([9, 1, 2, 4, 4, 5, 5]))
print (find_2nd_max([9, 9, 2, 4, 4, 5, 5]))