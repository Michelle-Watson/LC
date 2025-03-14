# 2. Stack (Using a List)

# Using list as a stack (LIFO)
stack = []
stack.append(10)  # Push
stack.append(20)
stack.append(30)

print("########## Stack (Using List) ##########")
# Big O: append() is O(1), pop() is O(1), peek() is O(1)
print("Pop:", stack.pop())  # 30 (pop)
print("Peek:", stack[-1])  # 20 (peek), last element
print("Stack after pop:", stack)  # Output: [10, 20]
print("\n")

############################################################

# 3. Queue (Using collections.deque)

from collections import deque

queue = deque([1, 2, 3, 4])  # Front: 1, Back: 4

print("########## Queue (Using deque) ##########")
# Big O: popleft() is O(1), append() is O(1)
print("Popped from front:", queue.popleft())  # Removes 1 from the front (left side)
print("Queue after pop:", queue)  # Output: deque([2, 3, 4])

queue.append(5)  # Adds 5 to the back (right side)
print("Queue after append:", queue)  # Output: deque([2, 3, 4, 5])
print("\n")

############################################################

# 4. Binary Search Tree (BST)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# Inserting into the tree follows the binary search property (left < parent < right).
def insert(node, key):
    if node is None:
        return Node(key)
    else:
        if key < node.value:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node


# In-order traversal prints the tree elements in sorted order.
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)


# Function to print the tree in a structured way with slashes
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        # Print the current node's value
        print(" " * (level * 4) + prefix + str(node.value))

        # Recursively print the left and right children
        if node.left or node.right:
            if node.left:
                print(" " * ((level + 1) * 4) + "/")
                print_tree(node.left, level + 1)
            else:
                print(" " * ((level + 1) * 4) + "/ None")

            if node.right:
                print(" " * ((level + 1) * 4) + "\\")
                print_tree(node.right, level + 1)
            else:
                print(" " * ((level + 1) * 4) + "\\ None")


# Example usage
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)

print("########## Binary Search Tree (BST) ##########")
# Big O: insert() is O(log n) for balanced tree, O(n) in worst case
print("Inorder traversal:")
inorder(root)  # Output: 20 30 40 50 70
print("\nTree Visualization:")
print_tree(root)
print("\n")

"""
In a balanced BST, the height of the tree is logarithmic in relation to the number of nodes, 
meaning the height is roughly O(log n) where n is the number of nodes in the tree.

For example, if the tree has 15 nodes, the height of a balanced tree will be around log₂(15) ≈ 4.
If the tree had 1,000 nodes, the height of the balanced tree would be around log₂(1000) ≈ 10.

The reason the height is logarithmic is that with each level of the tree, you "double" the 
number of possible nodes, like splitting the problem into two halves. 
This leads to a logarithmic growth in the tree height.

n = # of nodes

O(n) insert of unbalanced trees because you need to traverse down each leaf to insert

"""

############################################################

# 5. List (Dynamic Array)

# Dynamic array using Python's built-in list
lst = [1, 2, 3]
lst.append(4)  # Add to the end
lst.remove(2)  # Remove by value
print("########## List (Dynamic Array) ##########")
# Big O: append() is O(1), remove() is O(n) in the worst case (linear scan)
print("List after operations:", lst)  # Output: [1, 3, 4]
print("\n")

############################################################

# 6. Hash Table (Dictionary)
# Hash table using Python's built-in dictionary
# key value pairs
# fast lookups, insertions, and deletions on average in O(1) time.

hash_table = {"name": "Alice", "age": 25}

print("########## Hash Table (Dictionary) ##########")
# Big O: get() is O(1), pop() is O(1), insert() is O(1) on average
print("Value for 'name':", hash_table["name"])  # Output: Alice
print("Value for 'age':", hash_table.get("age"))  # Output: 25
hash_table.pop("age")  # Removes the key "age"
print("Hash table after pop:", hash_table)
print("\n")

############################################################

# 7. Trees with Variable Size (Generic Tree)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to hold children nodes

    def add_child(self, child):
        self.children.append(child)

    # Recursive method to print the tree
    def print_tree(self, level=0):
        # Print current node with indentation
        print(" " * (level * 4) + str(self.value))

        # Recursively print all children
        for child in self.children:
            child.print_tree(level + 1)


# Example usage
root = TreeNode(1)  # Root node
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

# Add children to root node
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

# Create more children for one of the root's children (child1)
child1.add_child(TreeNode(5))
child1.add_child(TreeNode(6))

child2.add_child(TreeNode(7))

print("########## Generic Tree (Variable Size) ##########")
# Big O: add_child() is O(1), print_tree() is O(n) where n is the number of nodes
print("Tree Structure:")
root.print_tree()
print("\n")

############################################################
