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


def branchSums(root):
    sums = []
    calc_branch_sum(root, 0, sums)
    return sums
	

# we need a helper function to call recursively

def calc_branch_sum(node, runningSum, sums):
    if node is None:
        return
    
    newRunningSum = runningSum + node.value
	# base case, if lead node, append runningSum
    if node.left is None and node.right is None:
	    sums.append(newRunningSum)
	    return 
    # if we are not at a leaf node, continue    
    if node.left:
		#traverse left
	    calc_branch_sum(node.left, newRunningSum, sums)
    if node.right:
		#traverse right
	    calc_branch_sum(node.right, newRunningSum, sums)
		


	
	
		

