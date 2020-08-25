class Stack():
    def __init__(self):
        self.counter = 0
        self.storage = {}

    def push(self, data):
        self.storage[self.counter] = data
        self.counter += 1

    def size(self):
        return self.counter

    def pop(self):
        if self.counter == 0:
            return
        self.counter -= 1
        del self.storage[self.counter]
    
    def is_empty(self):
        return len(self.storage) == 0

    def peek(self):
        return self.storage[self.counter-1]

    def print_elements(self):
        for i in self.storage:
            print(self.storage[i])




stack = Stack()
stack.push('A')
stack.push('B')
stack.push('C')
stack.pop()
stack.print_elements()
print('Size:', stack.size())
print(stack.is_empty())
print(stack.peek())
