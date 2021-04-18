# find an array of next greatest elements using stacks

'''
1. Iterate from last nth element to the 1st element

2. After reaching a certain index we will pop the stack till we get the greater element on top from the current element and 
that element will be the answer for current element

3. if stack is empty while doing pop -> store -1 in array for current idx
            
'''

def next_greatest_element(a):

    stack = []

    n = len(a)

    # init an array with the same size as the input array
    out = [-1 for i in range (n)] #S(N)

    # scroll backwards
    for i in range (n-1, -1, -1):  # O(N)

        # pop while stack is empty or stack top is less than current element
        while len(stack) > 0 and stack[-1] <= a[i]:
            stack.pop()

        # empty stack means no element exsist on right greater than curr element
        # if not empty next greater element in on top
        if len(stack) == 0:
            out[i] = -1
        else:
            # assign the top value to output array
            out[i] = stack[-1]

        # push the current element back into the stack
        stack.append(a[i])
   
    for i in range(n):
        print(a[i], " ---> ", out[i] )


next_greatest_element([11, 13, 21, 3])

# 13, 21, -1, -1

#   iteration   a[i]     stack[]                     output[stack[-1]]

#      0          3       [] -> 3                        -1

#      1         21      [3]-> [] -> 21                  -1

#      2         13      21 -> [21, 13]                  21

#      3         11       [21, 13] -> [21, 13, 11]        13




# brute force algorithms
# def next_greatest_element_brute(lst):
#     res = []
#     # Iterate list
#     for i in range(0, len(lst), 1):
#         # initialise nextGreatest to -1
#         next_greatest = -1
#         for j in range(i+1, len(lst), 1):
#             if lst[i] < lst[j]:
#                 # Update nextGreatest when greater value found
#                 next_greatest = lst[j]
#                 break
#         # append next greatest
#         res.append(next_greatest)
#         print(str(lst[i]) + " -- " + str(next_greatest))
#     return res