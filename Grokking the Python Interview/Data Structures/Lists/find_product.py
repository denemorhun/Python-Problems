''' Given a list, modify it so that 
each index stores the product of all 
elements in the list except the element 
at the index itself.

Sample Input #
arr = [1,2,3,4]
Sample Output #
arr = [24,12,8,6]

'''

# O(n2) solution
# def find_products(a):
#     s = len(a)

#     output = []
#     for i in range(s):
#         prod = 1
#         for j in range(s):
#             if i != j:
#                 prod *= a[j]
        
        
#         output.append(prod)

#     print(output)


# o(n) solution
# start from the left most index, and reach the index with product
# start from right, and calculte 
def find_products(a):
    s = len(a) #4

    output= [] # s(n)
    left = 1

    print("left")
    #loop 1 from left to current index O(n)
    for i in range(s):
        output.append(left)
        left *= a[i]
    # output = [ 1 1 2 6 ]

    print("right") # 1 4 12 24
    right = 1
    # loop 2 from right to current index O(n)
    # multiple the results and overwrite array
    for i in range(s-1, -1, -1): 
        # i         -> 3 2 1 0
        # output[i] -> 6 2 1 1 (in reverse)
        # right     -> 1 4 12 24
        # output[i] -> 6 8 12 24 (after multiplying above)
        print('i', i, 'output[i] ', output[i] , right)
        output[i] = right * output[i]
        right = right * a[i]

    print(output)
    


find_products([1, 2, 3, 4])
