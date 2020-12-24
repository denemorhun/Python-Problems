'''
A Node object has an integer data field, , and a Node instance pointer, , pointing to
 another node (i.e.: the next node in a list).

A removeDuplicates function is declared in your editor, which takes a pointer to the 
 node of a linked list as a parameter. Complete removeDuplicates so that it deletes 
 any duplicate nodes from the list and returns the head of the updated list.

Note: The  pointer may be null, indicating that the list is empty. Be sure to 
reset your  pointer when performing deletions to avoid breaking the list.

Input Format


Constraints

The data elements of the linked list argument will always be in non-decreasing order.


Your removeDuplicates function should return the head of the updated linked list. 


Sample Input

6
1
2
2
3
3
4
Sample Output

1 2 3 4 
Explanation

, and our non-decreasing list is . The values  and  both occur twice in the list
, so we remove the two duplicate nodes. We then return our updated (ascending) list
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

    def printhelper(self):
        print(f"     ->   has data {self.data}")

class LL: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  

    # prints the entire linkedlist, taking head as input
    def display(self,head):
        current = head

        # as long as the next node is not None, print and move to the next
        while current:
            print(current.data,end=' ')
            current = current.next

    # compare current node with next node and remove if identical
    def removeDuplicates(self,head):
        if head is None:
            return None

        curr_node = head
        next_node = curr_node.next
        
        while next_node is not None:

            # if data matches, update the next pointer
            if curr_node.data == curr_node.next.data:
                curr_node.next = curr_node.next.next

            else:
                curr_node = curr_node.next
            # next node here is just the pointer. how to get the actual node.
            next_node = curr_node.next

        return head


mylist = LL()

datalist = [1, 2, 2, 2, 4, 4, 5]

datalist2 = [1, 1, 1, 1, 1, 1, 1]

d3 = []

head=None

for i in range(len(d3)):
    data=d3[i]
    head=mylist.insert(head,data)    

print("original list")
mylist.display(head)

print('\nmodified list')
head=mylist.removeDuplicates(head)
mylist.display(head); 