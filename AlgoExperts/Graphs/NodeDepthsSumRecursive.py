''' Node Depths 
    Sum up all depths in the tree recursively

            1               | 0
                            
        2       3           | 1
                            
    4       5       7       | 2

    would equal 0 + 1 + 1 + 2 + 2 + 2

    We need to keep track of parents depth in order to construct all children's depth. 

'''



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
# where node provided is the root for the tree.
def nodeDepths(node, parentDepth=0):

    #base case, if 
    if node is None:
        return 0 

    else:
        return parentDepth + nodeDepths(node.left, parentDepth+1) + nodeDepths(node.right, parentDepth+1)


