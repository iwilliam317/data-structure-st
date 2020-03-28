class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next

list = LinkedList()
list.push(12)
list.push(2)
list.push(3)
list.print_list()