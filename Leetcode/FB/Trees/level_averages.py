'''
Task
Calculate the average of every level in a tree


            4   -> 4
          /  \
        6      10 -> 16 / 2 = 8
               \
                2 -> 2


# calculate the average at every level. 

'''
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(node, parentDepth=0):
  #base case, if 
    if node is None:
        return 0 

    else:
        return parentDepth + nodeDepths(node.left, parentDepth+1) + nodeDepths(node.right, parentDepth+1)

  



# def nodeDepths(root):
#     depths = []
#     # depth of the root node is 0
#     get_node_depth(root, 0, depths)
#     return sum(depths)
	

# # we need a helper function to call recursively
# def get_node_depth(node, currDepth, depths):
#     # base case
#     if node is None:
#         return

#     # if we are not at a leaf node, continue    
#     if node.left:
# 		#traverse left
#         newDepth = currDepth + 1
#         depths.append(newDepth)
#         get_node_depth(node.left, newDepth, depths)
#     if node.right:
# 		#traverse right
# 	    newDepth = currDepth + 1
# 	    depths.append(newDepth)
		
# 	    print (currDepth, newDepth, depths)
# 	    get_node_depth(node.right, newDepth, depths)

 # ############################################################
    # calculate the level averages of a binary tree using DFS
    # ############################################################

    # def calculate_avgs(self, bst):
    #     if bst:
    #         root = bst.value
            
    #     level_nodes = {}

    #     self._calculate_avgs(root, 0, level_nodes)

    #     for k, v in level_nodes.items():
    #         print(k, v)


    # def _calculate_avgs(self, root, depth, level_nodes):
        
    #     if root:
    #         if depth not in level_nodes.keys():
    #             level_nodes[depth] = root
    #         else:
    #             level_nodes[depth].append(self.value)
    #         depth += 1
    #         self._calculate_avgs(self.value.left, depth, level_nodes)
    #         self._calculate_avgs(self.value.right, depth, level_nodes)
        
    #     return level_nodes



bt = BinaryTree(4) # level 0

bt.left = 6
bt.right = 10 # level 1

bt.left.left = 2 # level 3

bt.right.left = 12
bt.right.right = 14 # level 2

print(nodeDepths(4, 0))
