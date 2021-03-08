''' Breadth First Search Graph Tree'''

        # basic algorithm

        # take the array as input

        # add current character to a list

        # check if it has a children nodes with while loop

        # if it has add to a queue

        # pop item 

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):

        output = []
        q = []

        for n in array:
            output.append(n)
            while n.children is not None:
                q.append(n.children.name)

            self.breadthFirstSearch(q.pop(0))








