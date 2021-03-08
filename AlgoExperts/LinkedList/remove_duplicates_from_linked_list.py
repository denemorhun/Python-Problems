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

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Even though this class says linkedlist, it's actually Node

def removeDuplicatesFromLinkedList(linkedList):
	
	# actually this is the head node
	currentNode = linkedList
	
	print("Starting with head node")
	
	while currentNode is not None:
		nextNode = currentNode.next
		
		print(currentNode.value)
		
		# if next node is equal to current node's value repeat loop
		while nextNode is not None and nextNode.value == currentNode.value:
			print('duplicate')
			nextNode = nextNode.next
			
		currentNode.next = nextNode
		currentNode = currentNode.next
		
	return linkedList