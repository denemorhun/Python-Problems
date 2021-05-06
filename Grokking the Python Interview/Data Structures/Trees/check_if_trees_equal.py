class BinaryTreeNode():
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 and root2:
        # base case, left children, right children
        return (root1 == root2) and are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)
   
    # If either root is None, return False
    else:
        return False












    # # if both trees are None, they are identical!
    # if root1 == None and root2 == None:
    #     return True
  
    # # if they are both not None, check children
    # if root1 != None and root2 != None:
    #     return (root1.data == root2.data and
    #           are_identical(root1.left, root2.left) and
    #           are_identical(root1.right, root2.right))
  
    return False
    

