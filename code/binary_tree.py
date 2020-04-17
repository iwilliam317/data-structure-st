class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = root
    

tree = BinaryTree(Node('A'))
tree.root.left = Node('B')
tree.root.right = Node('C')

tree.root.left.left = Node('D')
tree.root.left.right = Node('E')


print(tree.root.data)
print(tree.root.left.data)
print(tree.root.right.data)
print(tree.root.left.left.data)
print(tree.root.left.right.data)