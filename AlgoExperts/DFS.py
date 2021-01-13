# look for children in each node's children array recursively
# look for children before brethren

# O (V + E) complexity, O(V) for space

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

     # is the array empty? 
    def depthFirstSearch(self, array):
        # append to the array the node's name
	
        array.append(self.name)

        # call depthFirstSearch on all its children nodes. 

        for child in self.children:
            child.depthFirstSearch(array)
        
        return array




    def __str__(self) -> str:
        if self.children:
            for i in self.children:
                print(i)

        return self.name

Root = Node('A')
Root.addChild('B')
Root.addChild('C')

# print(Root.children[1])

# Root.depthFirstSearch()
