class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if node.left is None:
            node.left = Node(data)
        elif node.right is None:
            node.right = Node(data)
        else:
            self._insert(data, node.left)
            self._insert(data, node.right)

    def pre_order_print(self, start, transversal):
        if start:
            transversal += str(start.data+ " ")
            transversal = self.pre_order_print(start.left, transversal)
            transversal = self.pre_order_print(start.right, transversal)
        return transversal
    
    def in_order_print(self, start, transversal):
        if start:
            transversal = self.in_order_print(start.left, transversal)
            transversal += str(start.data + " ")
            transversal = self.in_order_print(start.right, transversal)
        return transversal

    def post_order_print(self, start, transversal):
        if start:
            transversal = self.post_order_print(start.left, transversal)
            transversal = self.post_order_print(start.right, transversal)
            transversal += str(start.data + " ")
        return transversal

#               A
#       B               C
#   D       E       F       G

tree = BinaryTree()
# tree.root.left = Node('B')
# tree.root.right = Node('C')

# tree.root.left.left = Node('D')
# tree.root.left.right = Node('E')

# tree.root.right.left = Node('F')
# tree.root.right.right = Node('G')

# print(tree.root.data)
# print(tree.root.left.data)
# print(tree.root.right.data)
# print(tree.root.left.left.data)
# print(tree.root.left.right.data)

tree.insert('A')
tree.insert('B')
tree.insert('C')
tree.insert('D')
tree.insert('E')


print(tree.pre_order_print(tree.root, ""))
# print(tree.in_order_print(tree.root, ""))
# print(tree.post_order_print(tree.root, ""))