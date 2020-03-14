class Stack():
    def __init__(self):
        self.counter = 0
        self.storage = {}

    def push(self, data):
        self.storage[self.counter] = data
        self.counter = self.counter + 1

    def size(self):
        return self.counter




stack = Stack()
stack.push(1)
print(stack.size())
