'''
Number of Visible Nodes
While viewing the tree from its left side and can see only the leftmost nodes at each level.
Return the number of visible nodes

Tip: We do not need to return the list of nodes, just the length.

Tip: We need to use breadth first search and count the first one on each level

Tip: We need to use a queue and 2 loops.
'''

class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 

def visible_nodes(self):

  current_node, q, left_nodes = self, [], []

  # first do the simple bfs algorithm
  q.append(current_node)

  while len(q) > 0:
    #level and number of nodes on a level are equal in a tree. 
    level = len(q)

    for i in range(level):
      current_node = q.pop(0)

      if i == 0:
        print('Most Left node on a level: ', current_node.val)
        left_nodes.append(current_node.val)

      if current_node.left:
          q.append(current_node.left)
      if current_node.right:
          q.append(current_node.right)
    
  return len(left_nodes)





# Run Tests function
def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  # Test 1
  root_1 = TreeNode(1)
  root_1.left = TreeNode(2)
  root_1.right = TreeNode(3)
  root_1.left.left = TreeNode(4)
  root_1.left.right = TreeNode(5)
  root_1.left.right.left = TreeNode(6)
  root_1.left.right.right = TreeNode(7)
  root_1.right.right = TreeNode(8)
  root_1.right.right.left = TreeNode(9)
  expected_1 = 4
  output_1 = visible_nodes(root_1)
  check(expected_1, output_1)

  # Test 2
  root_2 = TreeNode(10)
  root_2.left = TreeNode(8)
  root_2.right = TreeNode(15)
  root_2.left.left = TreeNode(4)
  root_2.left.left.right = TreeNode(5)
  root_2.left.left.right.right = TreeNode(6)
  root_2.right.left =TreeNode(14)
  root_2.right.right = TreeNode(16)
  expected_2 = 5
  output_2 = visible_nodes(root_2)
  check(expected_2, output_2)

  #Test 3
  root_3 = TreeNode(10)
  root_3.left = TreeNode(8)
  root_3.right = TreeNode(15)
  root_3.right.right = TreeNode(4)
  root_3.right.right.right = TreeNode(5)
  expected_3 = 4
  output_3 = visible_nodes(root_3)
  check(expected_3, output_2)
 

  
  