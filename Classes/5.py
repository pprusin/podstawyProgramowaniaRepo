# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, node):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search(key, node.left)
        return self._search(key, node.right)

tree = BST()
tree.insert(3)
tree.insert(1)
tree.insert(4)
print(tree.search(3) is not None)
print(tree.search(5) is None)
