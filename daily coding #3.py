import re

#Good morning! Here's your coding interview problem for today.
'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''
 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(tree):
    if tree == None:
        return "."
    d = []
    d.append(tree.val)
    d.append(serialize(tree.left))
    d.append(serialize(tree.right))
    return d

def deserialize(s):
    if s == ".":
        return None
    n = Node(s[0],deserialize(s[1]),deserialize(s[2]))
    return n
    '''
    d = re.compile('(^[a-z]+)\((.+)\),\((.+)\)')
    e = d.match(s)
    val = e[1] 
    left = e[2]
    right = e[3]   
    #split s into val, left, and right
   
    root = Node(val, deserialize(left), deserialize(right))
    # create a node with val as val, left=deserialize left, right = deserialize right
    #return 
     '''
    pass

node = Node('root', Node('left', Node('left.left')), Node('right'))
serialized = serialize(node)
print(serialized)
deserialized = deserialize(serialized)
print (deserialized)
assert deserialize(serialize(node)).left.left.val == 'left.left'