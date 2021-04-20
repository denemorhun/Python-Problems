''' Class that keeps track of min values '''

class my_stack():

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()

''' Push and pop to both a min stack and stack of values. '''

class min_stack():

    def __init__(self):
        self.stack = my_stack()
        self.min_stack = my_stack()

    def top(self):
        if self.stack.is_empty():
            return None
        return self.stack.top()

    def size(self):
        return self.stack.size()

    def pop(self):
        if not self.stack.is_empty():    
            self.min_stack.pop()
            return self.stack.pop()
        else:
            self.min_stack.clear()
            print("Cannot pop from empty stack.")
            return None

    # 
    def push(self, n):

        temp = []

        self.stack.push(n)

        if self.min_stack.is_empty():
            self.min_stack.push(n)
            print(self.min_stack.stack)

        # if number is more than min pop the whole stack, push larger value and reinsert emptied stack 
        elif n > self.min_stack.top():
                while not self.min_stack.is_empty() and n < self.min_stack.top():
                    temp.append(self.min_stack.pop())

                    print('temp array', temp)

                for item in temp:
                    self.min_stack.push(item)

        #if the number to be inserted is less than top value of min, append
        elif n <= self.min_stack.top() and not self.min_stack.is_empty():
            self.min_stack.push(n)
        
        print("Min_stack", self.min_stack.stack)

 

    def get_min(self):
        return self.min_stack.top()

    def get_stack(self):
        return self.min_stack.stack

    def __str__(self):
        return str(self.stack.stack)







ms = min_stack()
ms.push(4)
ms.push(5)
ms.push(1)
ms.push(99)
ms.push(-9)
ms.push(7)
ms.push(100000)
ms.push(3)

print("Our actual array", ms)

a = list(ms.get_stack())

# print('get min -> should be 2 -> ', ms.get_min())


# x = ms.pop()
# print('should be 3 is', x)



# print('top should be: 100000, ', ms.top())

# print(ms)

print('get min should be ->', min(a), ms.get_min())