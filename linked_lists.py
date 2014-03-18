# singly-linked lists
# ===================

class Node:
    """
    Node class for a singly-linked list.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def walk(head):
    """
    Iterative traversal.
    """
    cur = head
    while cur.next:
        print "{} --> {}".format(cur.value, cur.next.value)
        cur = cur.next

def rwalk(head):
    """
    Recursive traversal.
    """
    print head.value
    if head.next:
        rwalk(head.next)

def remove(head, value):
    """
    Given the head node, remove the node of a linked list with the given value.
    """
    cur = head
    prev = cur
    while cur:
        if cur.value == value:
            if cur.next:
                prev.next = cur.next
            else:
                prev.next = None
            break
        prev = cur
        cur = cur.next

def reverse(head):
    """
    Given the head node of a linked list, reverse the order of the list.
    """
    cur = head
    nodes = []
    while cur:
        nodes.append(cur)
        cur = cur.next
    for i in range(1, len(nodes)):
        print "{} --> {}".format(nodes[-i].value, nodes[-(i+1)].value)
        nodes[-i].next = nodes[-(i+1)]      
    nodes[0].next = None

def reverse_inline(head):
    """
    Reverses a linked list without using any significant additional memory.
    """
    cur = head
    last = None
    while cur:
        next = cur.next
        cur.next = last
        last = cur
        cur = next

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

# In [244]: walk(n1)
# 1 --> 2
# 2 --> 3
# 3 --> 4
# 4 --> 5

# In [245]: rwalk(n1)
# 1
# 2
# 3
# 4
# 5

# In [246]: remove(n1, 3)

# In [247]: walk(n1)
# 1 --> 2
# 2 --> 4
# 4 --> 5

# In [248]: reverse(n1)
# 5 --> 4
# 4 --> 2
# 2 --> 1

# In [249]: walk(n1)

# In [250]: walk(n5)
# 5 --> 4
# 4 --> 2
# 2 --> 1

# In [251]: reverse_inline(n5)

# In [252]: walk(n1)
# 1 --> 2
# 2 --> 4
# 4 --> 5


# doubly-linked lists
# ===================

class Node:
    """
    Node class for a doubly-linked list.
    """
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def walk_forward(head):
    """
    Forward traversal of a linked list, starting from the head node.
    """
    cur = head
    while cur.next:
        print "{} --> {}".format(cur.value, cur.next.value)
        cur = cur.next

def walk_backward(tail):
    """
    Backward traversal of a linked list, starting from the tail node.
    """
    cur = tail
    while cur.prev:
        print "{} --> {}".format(cur.value, cur.prev.value)
        cur = cur.prev

def remove(head, value):
    """
    Given the head node of a doubly-linked list, remove the node of
    with the given value.
    """
    cur = head
    while cur:
        if cur.value == value:
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            break
        cur = cur.next

n5 = Node(5)
n4 = Node(4, next = n5)
n3 = Node(3, next = n4)
n2 = Node(2, next = n3)
n1 = Node(1, next = n2)
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4

# In [263]: walk_forward(n1)
# 1 --> 2
# 2 --> 3
# 3 --> 4
# 4 --> 5

# In [264]: walk_forward(n3)
# 3 --> 4
# 4 --> 5

# In [265]: walk_backward(n5)
# 5 --> 4
# 4 --> 3
# 3 --> 2
# 2 --> 1

# In [266]: walk_backward(n3)
# 3 --> 2
# 2 --> 1

# In [267]: remove(n1, 3)

# In [268]: walk_forward(n1)
# 1 --> 2
# 2 --> 4
# 4 --> 5

# In [269]: walk_backward(n5)
# 5 --> 4
# 4 --> 2
# 2 --> 1