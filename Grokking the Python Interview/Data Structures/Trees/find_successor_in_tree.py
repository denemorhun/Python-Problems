''' 
Inorder -> LNR

NAIVE SOLUTION
Do a inorder traversal, 
get index of value to be found, 
and return value after 
'''
from collections import deque

class BinaryTreeNode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder_iterative(curr_node):

    output = []
    stack = deque()
    if curr_node is None:
        print("Tree is empty")
        return None

    # loop through while cn not null and stack not empty
    while curr_node != None or len(stack) != 0:
        if curr_node != None:
            stack.append(curr_node)
            curr_node = curr_node.left
            continue

        output.append(stack[-1].data)   
        
        curr_node = stack[-1].right
        stack.pop()

    return output

# method to get the value after in order traversal
def get_successor(array, val):
    if val not in array:
        return "Item doesn't exist"

    idx = array.index(val)

    if idx == len(array) - 1:
        return "Last item"

    return array[array.index(val)+1]     

# driver code

root = BinaryTreeNode(100)
root.left = BinaryTreeNode(50)
root.right = BinaryTreeNode(200)
root.left.left = BinaryTreeNode(25)
root.left.right = BinaryTreeNode(75)
root.left.left.right = BinaryTreeNode(35)

# array:  25 35 50 75 100 200 

array = inorder_iterative(root)
print(array)

# return item after first item
print(get_successor(array, 25))

# return item that doesn't exist
print(get_successor(array, 40))

# return item after last
print(get_successor(array, 200))