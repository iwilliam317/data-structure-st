class Queue():
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

        del self.storage[0]

    def print_elements(self):
        for i in self.storage:
            print(self.storage[i])




queue = queue()
queue.push(1)
queue.push(12)
queue.push(13)
queue.pop()
queue.print_elements()
print('Size:', Queue.size())
