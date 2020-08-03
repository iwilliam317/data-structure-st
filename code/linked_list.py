class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_after_node(self, previous_data, data):
        previous_node = self.search(previous_data)
        if previous_node:
            new_node = Node(data)
            new_node.next = previous_node.next
            previous_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def search(self, data):
        last_node = self.head
        while last_node.next and last_node.data != data:
            last_node = last_node.next
        return last_node
    
    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        
        previous_node.next = current_node.next
        current_node = None
    
    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.next)

    def reverse(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node

list = LinkedList()
list.append('A')
list.append('B')
list.append('C')
list.append('D')

# list.insert_after_node('B', 'E')
# list.delete('C')
# b = list.search('B')
# list.print_list()
# print(list.size(b))
list.reverse()
list.print_list()
# print(list.search('B'))