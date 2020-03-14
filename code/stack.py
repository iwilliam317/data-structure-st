class Stack():
    def __init__(self):
        self.counter = 0
        self.storage = {}

    def push(self, data):
        self.storage[self.counter] = data
        self.counter = self.counter + 1

    def size(self):
        return self.counter

    def pop(self):
        if self.counter == 0:
            return
        self.counter = self.counter - 1
        del self.storage[self.counter]

    def print_elements(self):
        for i in self.storage:
            print(self.storage[i])




stack = Stack()
stack.push(1)
stack.push(12)
stack.push(13)
stack.pop()
stack.print_elements()
print('Size:', stack.size())
