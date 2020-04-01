class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next


list = LinkedList()
list.append('A')
list.append('B')
list.append('C')
list.prepend('D')
list.print_list()