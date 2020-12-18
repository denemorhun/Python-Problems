''' Verify if the input string is a palindrome

A palindrome is a word, phrase, number, or other sequence of characters which reads
the same backwards and forwards. 

# first take each character in , enqueue it in a queue
# push that same character onto a stack. 
# Dequeue the first character from the queue and pop the top character off the stack
# then compare the two characters to see if they are the same
# While characters match, continue dequeueing, popping, and comparing each character until containers are empty 
# (a non-match means isn't a palindrome).

Write the following declarations and implementations:

Two instance variables: one for your , and one for your .
A void pushCharacter(char ch) method that pushes a character onto a stack.
A void enqueueCharacter(char ch) method that enqueues a character in the  instance variable.
A char popCharacter() method that pops and returns the character at the top of the  instance variable.
A char dequeueCharacter() method that dequeues and returns the first character in the  instance variable.

Constraints

is composed of lowercase English letters.

Sample Input

racecar
Sample Output

The word, racecar, is a palindrome
'''

import sys
import collections

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = [] 
        
    def pushCharacter(self, ch):
        self.stack.append(ch)
        
    def enqueueCharacter(self, ch):
        self.queue.insert(0, ch)
        
    def popCharacter(self):
        return self.stack.pop()
        
    def dequeueCharacter(self):
        return self.queue.pop()
        
    # Write your code here

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    




def main():
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp", "tca", "bbb", "bbb"]

    print(find_palindromes(words))

if __name__ == '__main__': main()
