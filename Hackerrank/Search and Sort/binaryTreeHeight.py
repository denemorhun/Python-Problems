'''
Task
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, , pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree:
The first line contains an integer, , denoting the number of nodes in the tree.
Each of the  subsequent lines contains an integer, , denoting the value of an element that must be added to the BST.

Output Format

The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

Sample Input

7
3
5
2
1
4
6
7
Sample Output

3

LEVEL ORDER
Hint: You'll find a queue helpful in completing this challenge.

Function Description

Complete the levelOrder function in the editor below.

levelOrder has the following parameter:
- Node pointer root: a reference to the root of the tree

Prints
- Print node.data items as space-separated line of integers. No return value is expected.
'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class BST:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    # compare left and right trees and take maximum
    def getHeight(self,root):
        # Base case. 
        if root is None:
            return -1
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        return 1 + max(left_height, right_height)

    ##################################
    # Node -> Left -> Right 
    ##################################
    def levelOrder(self, root):
        q = [root] if root else []
    
        while q:
            node = q.pop()

            if node.left:
                q.insert(0, node.left)
            if node.right:
                q.insert(0, node.right)
                
            print(str(node.data), end=" ")

T=int(input())

myTree=BST()

root=None

for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)


height=myTree.getHeight(root)
print("Height of the tree:", height)        

myTree.levelOrder(root)