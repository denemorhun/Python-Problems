class MyStack:

    def __init__(self):
        self.stack_list = []
        pass

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

    def __str__(self):
        items = [item for item in self.stack_list]
        return str(items)


    