'''
Task
Calculate the sum of the branch until the leaf nodes in a tree

# keep track of running sum (all nodes preceding a child node)
'''
# This is the class of the input root. Do not edit it.

# This is the class of the input root. Do not edit it.


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    depths = []
    # depth of the root node is 0
    get_node_depth(root, 0, depths)
    return sum(depths)
	

# we need a helper function to call recursively
def get_node_depth(node, currDepth, depths):
    # base case
    if node is None:
        return

    # if we are not at a leaf node, continue    
    if node.left:
		#traverse left
        newDepth = currDepth + 1
        depths.append(newDepth)
        get_node_depth(node.left, newDepth, depths)
    if node.right:
		#traverse right
	    newDepth = currDepth + 1
	    depths.append(newDepth)
		
	    print (currDepth, newDepth, depths)
	    get_node_depth(node.right, newDepth, depths)

