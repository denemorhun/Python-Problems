''' 

Inorder -> LNR

Pseudo-code

initialize the current_node as root.
create an empty stack stk.
Push the current_node in stk and,
 set current_node = current_node->left until current_node becomes NULL.
if stk is not empty and current_node == NULL then
  Print the top element from stk
  Pop the top element from stk and set current_node = element_popped->right
  go to step 3
if current_node is null and stack is empty then algorithm terminates.

'''
from collections import deque


class BinaryTreeNode():
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder_iterative(curr_node):

    result = " "

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

        result += str(stack[-1].data) + " "    
        
        curr_node = stack[-1].right
        stack.pop()

    return str(result)


root = BinaryTreeNode(100)
root.left = BinaryTreeNode(50)
root.right = BinaryTreeNode(200)
root.left.left = BinaryTreeNode(25)
root.left.right = BinaryTreeNode(75)
root.left.left.right = BinaryTreeNode(35)

print(inorder_iterative(root))

