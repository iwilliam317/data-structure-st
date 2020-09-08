class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_queue(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
    
    def remove(self):
        if self.head:
            self.head = self.head.next
            return

            

queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.remove()
queue.remove()
queue.remove()
queue.add(1)
queue.print_queue()