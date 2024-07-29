
# Data-Science  
This repository tuples and stacks
 ## Tuples
                   Definition of Tuples
A tuple is an ordered data structure that is used to store different items in a single variable. Tuples are immutable.
Tuples can contain elements of different data types, for example, strings, integers, 
Tuples are immutable, which allows them to be used as dictionary keys. 
Tuples are accessed using their indices.

## Stacks
                   Definition of Stacks
A stack is a data structure where adding a new element and removing an existing element takes place at the same end known as "top of the stack.
Elements are added one by one.
Stacks use the LIFO-FILO concept, meaning the first element to be added is the last one to be added, and the last one to be added is the last one to be removed.
-Stacks are ordered
- Accessing an item in the middle would require you to remove all the items above it till you get to the item you want.
- Stacks can contain duplicate values

  ##Queues
  # Definition of queues
  A queue is a data structure that is used for managing and storing data in a specific order.


##Binary search tree
# Definition of a binary Search tree
# It is a data structure used to store data in a sorted manner.
# Each node in a Binary Search Tree has at most two children, a left child and a right child, with the left child containing values less than the parent node and the right child containing values greater than the parent node. 
# Efficient searching: O(log n) time complexity for searching
# Ordered structure: Elements are stored in sorted order, making it easy to find the next or previous element.
# Dynamic insertion and deletion: Elements can be added or removed efficiently.
# Space efficiency: BSTs store only the key values, making them space-efficient.

##  The code defines a `Node` class for creating new nodes in the binary tree. Each node has a value (`key`) and pointers to left and right child nodes.

# The `insert` function is used to add new nodes to the tree. It takes the current root node and a key as arguments. If the tree is empty, it creates a new node. Otherwise, it recursively finds the correct position for the new node based on the comparison between the key and the existing nodes' values.

# The `search` function searches for a node with a specific key in the tree. It returns the node if found; otherwise, it returns `None`.
