class Queue():
    def __init__(self):
        self.counter = 0
        self.index = 0
        self.storage = {}

    def push(self, data):
        self.storage[self.counter] = data
        self.counter = self.counter + 1

    def size_queue(self):
        return self.counter

    def pop(self):
        del self.storage[self.index]
        self.index = self.index + 1
        self.counter = self.counter - 1

        if self.counter == 0:
            self.index = 0

    def print_elements(self):
        for i in self.storage:
            print(self.storage[i])




queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
queue.pop()
queue.pop()
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()

queue.print_elements()
print('Size:', queue.size_queue())
