"""
To visit nodes 1-9 in order using in-order traversal, the tree would be:
               [9] 
               /           
              /         
            [6]         
            / \        
           /   \      
         [2]    [7]      
         /\      \    
        /  \      \    
       /    \      \ 
    [1]     [5]     [8]       
            /      
          [4]      
          /    
        [3]
"""

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
        pre_order_traversal(node.left)
    if node.right:
        pre_order_traversal(node.right)

def in_order_traversal(node):
    """
    Prints the values of the nodes in a binary tree as encountered in an
    'in-order' recursive traversal of the tree.
    """
    if node.left:
        in_order_traversal(node.left)
    print node.value
    if node.right:
        in_order_traversal(node.right)

def iterative_in_order_traversal(node):
    """
    Prints the values of the nodes in a binary tree as encountered in an
    'in-order' traversal of the tree without using recursion.
    """
    s = []
    done = False
    while node or s != []:
        if node:
            s.append(node)
            node = node.left
        else:
            node = s.pop()
            print node.value
            node = node.right
            
# build the tree
for i in range(1,10):
    vars()['n'+str(i)] = Node(i)

n2.left = n1
n2.right = n5
n5.left = n4
n4.left = n3
n6.left = n2
n6.right = n7
n7.right = n8
n9.left = n6

# In [24]: pre_order_traversal(n9)
# 9
# 6
# 2
# 1
# 5
# 4
# 3
# 7
# 8

# In [25]: in_order_traversal(n9)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# In [26]: iterative_in_order_traversal(n9)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
