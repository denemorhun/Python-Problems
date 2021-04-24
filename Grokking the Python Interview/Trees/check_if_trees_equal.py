class BinaryTreeNode():
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def are_identical(root1, root2):
    # if both trees are None, they are identical!
    if root1 == None and root2 == None:
        return True
  
    # if they are both not None, check children
    if root1 != None and root2 != None:
        return (root1.data == root2.data and
              are_identical(root1.left, root2.left) and
              are_identical(root1.right, root2.right))
  
    return False
    
BT1 = BinaryTreeNode(5)
BT1.left = 4
BT1.right = 6

print(BT1.data)

BT2 = BinaryTreeNode(5)
BT2.left = 4
BT2.right = 6

print(BT2.data)

are_identical(BT1, BT2)

