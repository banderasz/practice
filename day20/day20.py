"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

    def linked_list_len(self):
        root = self
        i = 0
        while root:
            i += 1
            root = root.next
        return i


A = Node(3, Node(7, Node(8, Node(10))))
B = Node(99, Node(80, Node(1, Node(8, Node(10)))))


first_intersect = None
while True:
    if A.linked_list_len() > B.linked_list_len():
        A = A.next
    elif A.linked_list_len() < B.linked_list_len():
        B = B.next
    elif A.linked_list_len() == B.linked_list_len() and A.val == B.val:
        if not first_intersect:
            first_intersect = A.val
        A = A.next
        B = B.next
    elif A.linked_list_len() == B.linked_list_len() and A.val != B.val:
        first_intersect = None
        A = A.next
        B = B.next
    if A is None or B is None:
        break


print(first_intersect)
