from Node import Node

class LinkedList():
    def __init__(self):
        self.head_node = None

    # return headnode of the LinkedList
    def get_head(self):
        return self.head_node

    # Return true if empty
    def is_empty(self):
         # Check whether the head is None
        if(self.head_node is None): 
            return True
        else:
            return False

    def insert_at_tail(self, data):

        # if LL is empty, set value as headnode
        if self.is_empty():
            self.head_node = Node(data)
        # if list is not empty, set current node to head
        else:
            curr_node = self.get_head()

            # if list not empty, traverse the list to the last node
            while curr_node.next_element != None:
                curr_node = curr_node.next_element

            # Set the nextElement of the previous node to new node
            curr_node.next_element = Node(data)
            curr_node.next_element.next_element = None

    # Traverse the Linkedlist and find value at O(n)
    def search (self, value):
        # IF LL is empty value cannot be found
        if self.is_empty():
            return None
           
        curr_node = self.head_node

        while curr_node != None:
            # check if value is what we are looking for 
            if curr_node.data == value:
                print("Found value", value)
                return True

            curr_node = curr_node.next_element

        return False


    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

