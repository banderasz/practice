"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.unival = False
        self.cus = self.count_unival_subtree()


    def count_unival_subtree(self):
        if self.left is None and self.right is None:
            self.unival = True
            return 1
        else:  # all the nodes has 0 or 2 child
            if self.left.val == self.val and self.right.val == self.val and self.left.unival and self.right.unival:
                return self.left.cus + self.right.cus + 1
            else:
                return self.left.cus + self.right.cus


rNode = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(rNode.cus)


