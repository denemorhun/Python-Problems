'''
Task
Calculate the sum of the branch until the leaf nodes in a tree

# keep track of running sum (all nodes preceding a child node)
'''
# This is the class of the input root. Do not edit it.

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    sum_of_depths = 0
    # depth of the root node is 0
    calc_node_depths(root, 0, sum_of_depths)
    return sum_of_depths
	

# we need a helper function to call recursively
def calc_node_depths(node, currDepth, s):
    if node is None:
        return

    newDepth = currDepth + 1


    # base case: if all nodes have been processed we've found all nodes.
    
    if node.left and node.value:
        1 + calc_node_depths(node.left, depth, s)

    if node.right and node.value:
        1 + calc_node_depths(node.right, depth, s)

	# base case, if lead node, append runningSum
    if node.left is None and node.right is None:
	    sums.append(newRunningSum)
	    return 
    # if we are not at a leaf node, continue    
    if node.left:
		#traverse left
	    calc(node.left, newRunningSum, sums)
    if node.right:
		#traverse right
	    calc(node.right, newRunningSum, sums)
		


	
	
		

