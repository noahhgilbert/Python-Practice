'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   0   0
  / \
 1   1
 '''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = Node(1, 
        Node(1), 
        Node(1, 
            Node(1, 
                Node(1), 
                Node(1)), 
            Node(1)))

def count_univals(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    # if left or right is none, pretend their val is same as current node val dor determining whether unival
    count = count_univals(node.left) + count_univals(node.right)
    left = node.val if node.left is None else node.left.val
    right = node.val if node.right is None else node.right.val
    if node.val == left and node.val == right:
        return 1 + count
    else:
        node.val = -1
        return count

print(count_univals(tree))