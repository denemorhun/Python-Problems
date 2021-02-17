# MEDIUM
'''
Add two numbers that are represented by a 
linkedlist but written backwards

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

The pseudocode is as following:

Initialize current node to dummy head of the returning list.
Initialize carry to 00.
Initialize pp and qq to head of l1l1 and l2l2 respectively.
Loop through lists l1l1 and l2l2 until you reach both ends.
Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
Set sum = x + y + carrysum=x+y+carry.
Update carry = sum / 10carry=sum/10.
Create a new node with the digit value of (sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
Advance both pp and qq.
Check if carry = 1carry=1, if so append a new node with digit 11 to the returning list.
Return dummy head's next node.
Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.


'''
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        output = ListNode()
        nextNode = output
        # nextNode = output.next
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            s = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry)//10

            # nextNode = ListNode(s)
            nextNode.next = ListNode(s)
            nextNode = nextNode.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
            # return output.next
        return output.next

  # driver code
    if __name__ == '__main__':
        input = ""

        #l1 = ListNode

        result = addTwoNumbers([2,4,3], [5,6,4])

        print(result)