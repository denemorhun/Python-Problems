'''



'''
# This is the class of the input root. Do not edit it.

class BST:
    ############################################################
    # Init tree with value, left and right
    ############################################################
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    ############################################################
    # Insert value into Tree, if less than node, insert to left
    # if value greater than, insert to the right tree
    ############################################################
    def insert(self, value):

        if value is None:
            return self
        # if inserted value is greater than or equal to head, insert to right tree
        if value < self.value:
            # if left child is None, at leaf node, place value here
            if self.left is None:
                self.left = BST(value)
            # recursively call insert if left node exists therefore not leaf node
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    '''
    Traverse down to the leaf nodes. If value exists, it will be found 
    before all leaf nodes are reached. 
    '''
    ############################################################
    # Verify if value is in the tree
    ############################################################
    def contains(self, value):
        currentNode = self
        
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
    
    ############################################################
    # Find the min value (most left) in the BST
    ############################################################
    def find_min_val(self):
        if self.left:
            return self.left.find_min_val()
        else:
            return self.value

    ############################################################
    # Find max value in the BST (most right)
    ############################################################
    def find_max_val(self):
        if self.right:
            return self.right.find_max_val()
        else:
            return self.value
            

    ''' Traverse to leaf nodes to search for node to be removed
        # if leaf node is reached, value to be removed doesn't exist
    
        # If no child node or only 1 child node, set node to null
        
        # elif node has two children nodes, rebalance
            # search for left most value in the right subtree for minval
            # Replace node with minval
            # set minval to null '''
    # ############################################################
    # Search and remove a value from tree
    # ############################################################
    def remove(self, value):
        """
        :type bst: bst
        :type key: int
        :rtype: bst
        """

        prev, curr = None, self
        bst = self
        
        # 1. find the node
        while curr and curr.value != value:
            prev = curr
            curr = curr.left if value < curr.value else curr.right

        
        # 2. check if node exists
        if curr is None:
            return self
        
        # 3. check if there exists a successor to the node
        if curr.right is None:
            # 4. check if the node is the root
            if curr is bst:
                return bst.left
            
            # node is internal to the tree
            if prev.left is curr:
                prev.left = curr.left
            else:
                prev.right = curr.left
                    
            curr.left = None
            return bst

        # 5. find inorder successor
        prev_succ, succ = curr, curr.right
        while succ.left:
            prev_succ = succ
            succ = succ.left
        
        # 6. swap the values
        curr.value = succ.value
        
        # 7. handle the right child of the successor
        if prev_succ is curr:
            prev_succ.right = succ.right
        else:
            prev_succ.left = succ.right
            
        succ.right = None
        
        return bst

    # ############################################################
    # # Print Tree in Preorder -> Left, Root, Right
    # ############################################################
    def print_in_order(self, bst):
        if bst:
            self.print_in_order(bst.left)
            print(bst.value)
            self.print_in_order(bst.right)


    # ############################################################
    # # Print Tree in Preorder -> Node, Left, Right
    # ############################################################
    def print_pre_order(self, bst):
        if bst:
            print(bst.value)
            self.print_pre_order(bst.left)
            self.print_pre_order(bst.right)

    # ############################################################
    # # Return size of the tree
    # ############################################################
    def sizeof(self, bst):
        if bst is None:
            return 0
        else:
            return 1 + self.sizeof(bst.left) + self.sizeof(bst.right)

   

    # ############################################################
    # calculate the branch sums of a tree
    # ############################################################
    # def branchSums(self, root):
    #     sums = []
    #     self._calc_branch_sum(root, 0, sums)
    #     return sums

    # # helper function
    # def _calc_branch_sums(self, node, runningSum, sums):
    #     if node is None:
    #         return
    
    #     newRunningSum = runningSum + node.value
	    
    #     # base case, if lead node, append runningSum
    #     if node.left is None and node.right is None:
	#         sums.append(newRunningSum)
	#         return 
    
    #     # if we are not at a leaf node, continue    
    #     if node.left:
	# 	    #traverse left
	#         calc_branch_sum(node.left, newRunningSum, sums)
    #     if node.right:
	# 	    #traverse right
	#         calc_branch_sum(node.right, newRunningSum, sums)

############################################################
# Driving code
############################################################
def main():
    # when we initialize, we must provide a head node
    bst = BST(10)
    bst.insert(11)
    bst.insert(9)
    bst.insert(6)
    bst.insert(56)
    bst.insert(3)

    # print in order and preorder
    bst.print_in_order(bst)

    # print("try to print pre_order")
    # bst.print_pre_order()

    # contains test
    # n = 57
    # print(f"Check if {n} is in the tree: ")
    # print(bst.contains(n))

    # # print the size of tree
    print("The size of the tree:", bst.sizeof(bst))

    # find min val test
    # print("The min val in tree is:")    
    # print(bst.find_min_val())

    # print(bst.find_max_val())

    # remove test
    bst.remove(10)
    bst.remove(3)
    bst.remove(56)
    bst.print_in_order(bst)


    # n = 56
    # bst.remove(n)
    # print("Check if 57 is in tree:", bst.contains(n))
    # print(bst.right.right.value)


if __name__ == "__main__":
    main()

