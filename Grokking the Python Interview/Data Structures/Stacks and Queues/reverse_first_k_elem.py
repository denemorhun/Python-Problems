''' 
Implement the function reverseK(queue, k) which takes a 
queue and a number “k” as input and reverses the first “k” 
elements of the queue.

A stack can be used to reverse a queue.

O(n+k)
'''

from queues import MyQueue
from stack import MyStack


def reverseK(queue, k):

    if k < 0 or k > queue.size() or queue.is_empty():
        return None

    stack = []
    out = MyQueue()
    # deq k times onto a stack
    # pop from stack k times and enq

    for i in range(k):
        stack.append(queue.dequeue())

    print(stack)

    while len(stack) > 0: 
        out.enqueue(stack.pop())
    
    while queue.size() > 0:
        out.enqueue(queue.dequeue())

    return out

    

# Driving code
inputq = MyQueue()
inputq.set([1,2,3,4,5,6,7,8,9,10])

print(reverseK(inputq, 5))