# Binary Search Tree Implementation in Python

This repository contains the implementation of a Binary Search Tree (BST) in Python.

## How to use

1. Clone this repository.
2. Run the `bst.py` file with Python.
3. Use the `insert()` method to add nodes to the tree and `inorder_traversal()` to display the tree in sorted order.

## Example

```python
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

bst.inorder_traversal(bst.root)