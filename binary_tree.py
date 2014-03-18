class Node:
    """
    Node class for binary trees.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(node):
    """
    Prints the values of the nodes in a binary tree as encountered in a
    'pre-order' recursive traversal of the tree.
    """
    print node.value
    if node.left:
        recursive_print_tree(node.left)
    if node.right:
        recursive_print_tree(node.right)

def in_order_traversal(node):
    """
    Prints the values of the nodes in a binary tree as encountered in an
    'in-order' recursive traversal of the tree.
    """
    if node.left:
        recursive_print_tree(node.left)
    print node.value
    if node.right:
        recursive_print_tree(node.right)

n5 = Node(5)
n4 = Node(4, left=n5)
n3 = Node(3)
n2 = Node(2, left=n4, right=n3)
n1 = Node(1, right=n2)

# In [233]: pre_order_traversal(n1)
# 1
# 5
# 4
# 2
# 3

# In [234]: in_order_traversal(n1)
# 1
# 5
# 4
# 2
# 3