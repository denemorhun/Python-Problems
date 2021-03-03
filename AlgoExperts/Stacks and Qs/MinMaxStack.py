''' Min Max Stack Construction'''

from collections import deque as deck

class MinMaxStack:

    #constructor
    def __init__(self):
        self.stack = deck()
        self.minmaxstack = deck()

    def __str__(self):
        return f"{self.stack}"

    def peek(self):
        print(self.stack[-1])
        return self.stack[-1]

    def pop(self):
        
        self.minmaxstack.pop()
        return self.stack.pop()

    def push(self, number):

        self.stack.append(number)

        if len(self.minmaxstack) > 0:
            maxval = self.minmaxstack[-1][1]
            minval = self.minmaxstack[-1][0]

            if number < minval:
                self.minmaxstack.append( (number, maxval) )
            elif number >= maxval:
                self.minmaxstack.append( (minval, number) )
        else:
            self.minmaxstack.append( (number, number) ) 

    def getMin(self):
        return self.minmaxstack[-1][0]

    def getMax(self):
        return self.minmaxstack[-1][1]