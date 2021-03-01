'''
Task
Build a BST tree

# All values to the left must have a value less than node

# All values to the right must have a value more than node

# For insertion, add the value once you reach a leaf (ie None) node

# for searching, if you reach a leaf node before matching the value, value is not in BST

# delete head node, and check if it has any children for reconnection


'''
# This is the class of the input root. Do not edit it.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 
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

    # traverse down to the leaf nodes. If value exists, it will be found 
    # before all leaf nodes are reached. 
    def contains(self, value):

        if value is None:
            return False

        # traverse the left side of tree and avoid all nodes on right
        if value < self.value:
            # if you reach a leaf node, value must not exist
            if self.left is None:
                print(f"Reached leaf node, {value} doesn't exist")
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            # if you reach a leaf node onthe right, value must not exist
            if self.right is None:
                print(f"Reached leaf node, {value} doesn't exist")
                return False
            else:
                return self.right.contains(value)
        else:
            print("found value", value)
            return True

    
    '''
    # Traverse to leaf nodes to search for node to be removed
        # if leaf node is reached, value to be removed doesn't exist
    
        # If no child node or only 1 child node, set node to null
        
        # elif node has two children nodes, rebalance
            # search for left most value in the right subtree for minval
            # Replace node with minval
            # set minval to null

    '''

    def find_min_val(self, bst):
        if bst.left:
            self.find_min_val(bst.left)
        else:
            print(bst.value)
            return bst.value

    def find_max_val(self, bst):
        if bst.right:
            self.find_max_val(bst.right)
        else:
            return bst.value
            
    

    # def remove(self, value):
    #     if value is None:
    #         return self

    # # Search for value

    #     # traverse left subtree
    #     if value < self.value:
    #         # reached leaf node, value inexistent
    #         if self.left is None:
    #             print("Value does not exist, unable to remove")
    #             return self
    #         else:
    #             return self.left.remove(value)

    #     # traverse right subtree
    #     if value > self.value:
    #         # reached leaf node, value inexistent
    #         if self.right is None:
    #             print("Value does not exist, unable to remove")
    #             return self
    #         else:
    #            return self.right.remove(value)

    # # found value, check if it has children
    #     if value == self.value:
    #         print("Target value found")
    #         # Has two children
    #         if self.right and self.left:
    #             # track minval from right subtree
    #             if self.right.left is None:
    #             minval = self.right
    #             # find minval from right subtree
    #             if self.right.left is not None:
    #                 minval = self.remove(self.right.left)
    #             else:
    #                 # set the minval of right subtree to null
    #                 self.right.left = None

    #                 # replace value with minval
    #                 self.value = minval
                   

    # #         # Has 0 or 1 children, 
    # #         else:
    # #             # if only right child exists
                
    # #             if self.right is not None:
    # #                 print("only right child exists")
    # #                 self.value = self.right
    # #                 self.right = self.right.left
    # #             # if only left child exists
    # #             elif self.left is not None:
    # #                 print("if only left child exists")
    # #                 self.value = self.left
    # #                 self.left = self.left.left
    # #             # if no children
    # #             else:
    # #                 self.value = None

    #     return self

    # Print Left, Root, Right
    def print_in_order(self, bst):
        if bst:
            self.print_in_order(bst.left)
            print(bst.value)
            self.print_in_order(bst.right)

    def print_pre_order(self, bst):
        if bst:
            print(bst.value)
            self.print_pre_order(bst.left)
            self.print_pre_order(bst.right)

    def sizeof(self, bst):
        if bst is None:
            return 0
        else:
            return 1 + self.sizeof(bst.left) + self.sizeof(bst.right)

def main():
    # when we initialize, we must provide a head node
    bst = BST(10)
    bst.insert(11)
    bst.insert(9)
    bst.insert(6)
    bst.insert(56)

    # print(bst.value)

    print("try to print inorder")
    bst.print_in_order(bst)

    print("try to print pre_order")
    bst.print_pre_order(bst)

    # contains test
    n = 57
    print(f"Check if {n} is in the tree: ")
    print(bst.contains(n))

    # print the size of tree
    print("The size of the tree:", bst.sizeof(bst))

    # find min val test
    print("The min val in tree is:")    
    print(bst.find_min_val(bst))

    # # remove test

    # n = 56
    # bst.remove(n)
    # print("Check if 57 is in tree:", bst.contains(n))
    # print(bst.right.right.value)



if __name__ == "__main__":
    main()

