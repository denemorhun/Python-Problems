from typing import Deque
from stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean

class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here

    # Inserts Element in the Queue
    def enqueue(self, value):
        self.main_stack.push(value)
        return True

    # Removes Element From Queue
    def dequeue(self):
        # Write your code here
        temp_stack = MyStack()
        
        while not self.main_stack.size() == 1:
            temp_stack.push(self.main_stack.pop())
        
        popped_item = self.main_stack.pop()

        while not temp_stack.is_empty():
            self.main_stack.push(temp_stack.pop())

        return popped_item

    def __str__(self):
        return str(self.main_stack)


nq = NewQueue()

nq.enqueue(1)
nq.enqueue(2)
nq.enqueue(3)
nq.enqueue(4)
nq.enqueue(5)

val = nq.dequeue()
print(nq)
print(val)
