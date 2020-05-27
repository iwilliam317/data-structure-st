class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self, data):
        self.root = Node(data)

    def height(self):
        if self.root is None:
            return 0
        return self._height(self.root, 0)
    
    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_tree = self._height(current_node.left, current_height + 1)
        right_tree = self._height(current_node.right, current_height + 1)

        return max(left_tree, right_tree)
    
    def inorder_traversal(self, node, traversal):
        if node:
            traversal = self.inorder_traversal(node.left, traversal)
            traversal += str(node.data) + ' '
            traversal = self.inorder_traversal(node.right, traversal)
        return traversal
    
    def insert(self, data):
        if self.root is None:
            self.root = data
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print('Number %s already in tree' %(data))

bst = BST(22)

bst.insert(3)
bst.insert(41)
bst.insert(13)
bst.insert(30)
bst.insert(30)

print(bst.inorder_traversal(bst.root, ''))
print(bst.height())

