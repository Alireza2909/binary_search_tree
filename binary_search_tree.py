# Binary Search Tree (BST) Implementation in Python

class Node:
    def __init__(self, data):
        self.data = data  # Node data
        self.left = None  # Left child
        self.right = None  # Right child

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Root of the tree

    # Method to insert a node in the BST
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node  # If tree is empty, make new node the root
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    # Method to print the BST (Inorder Traversal)
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# Example usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal of BST:")
bst.inorder_traversal(bst.root)  # Output: 20 30 40 50 60 70 80