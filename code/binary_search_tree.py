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
    
    # print option 1
    # def print_bst(self, node, traversal):
    #     if node:
    #         traversal = self.print_bst(node.left, traversal)
    #         traversal += str(node.data) + ' '
    #         traversal = self.print_bst(node.right, traversal)
    #     return traversal

    # print option 2
    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
    
    def _print_tree(self, current_node):
        if current_node is None:
            return
        self._print_tree(current_node.left)
        print(current_node.data)
        self._print_tree(current_node.right)

    
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
    
    def search(self, data):
        if self.root:
            return self._search(data, self.root)
        return False

    def _search(self, data, current_node):
        if current_node.data == data:
            return True
        elif data < current_node.data and current_node.left:
            return self._search(data, current_node.left)
        elif data > current_node.data and current_node.right:
            return self._search(data, current_node.right)
        else:
            return False

bst = BST(22)

bst.insert(3)
bst.insert(41)
bst.insert(13)
bst.insert(30)
bst.insert(30)

# print(bst.print_bst(bst.root, ''))
print(bst.print_tree())
print(bst.height())
print(bst.search(3))
print(bst.search(33))

