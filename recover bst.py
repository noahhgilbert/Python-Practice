        5
       / \
     3     7
    / \    / \
   1   4  6   8


        5
       / \
     4     7
    / \    / \
   1   3  6   8


        8
       / \
     3     7
    / \    / \
   1   4  6   5


class Node:
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.l = left
        self.r = right

def print_tree(root):
    if root is None:
        return
    print_tree(root.l)
    print(root.v)
    print_tree(root.r)

def swap(a, b):
    tmp = a.v
    a.v = b.v
    b.v = tmp

def find_mistake(root):
    helper(root,)


def helper(tree, max_or_min):
    if tree is None:
        return
    left_min, left_max 
    left_val = helper(tree.l)
    if  left_val > tree.v:
        print ("Out of order {0} {1}").format(left_val, tree.v)
    right_val = helper(tree.r)
    if right_val < tree.v

if __name__=="__main__":
    root = Node(3,Node(1),Node(4,Node(2)))
    print ("test")
    print_tree(root)


    swap (root, root.r.l)
    print_tree(root)
    