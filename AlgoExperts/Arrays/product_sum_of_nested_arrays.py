''' calculate product sum '''

# input: special array of integers, or other special arrays of integers.
# return sum of all integers and sub-array integers * depth
# depth is level of nested
# solve by recursion

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

def productSum(array, depth=1):
    # anytime we call this recursive function, we start with sum 0
    total = 0
    
    for elem in array:
        if type(elem) is list:
            depth += 1
            total += productSum(elem, depth)
        else:
            total += elem

		
if __name__ == '__main__':
        input = [1, 2, [4, 5]]

        print(productSum(input))


        