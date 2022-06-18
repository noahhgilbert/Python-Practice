'''
This question was recently asked by Google.
Given two sorted linked lists, merge them in order.
This can be done recursively and iteratively. See if you can get both solutions.
'''
import random
from pprint import pprint

def merge_list_iterative( list1, list2):
    tmp1 = list1
    tmp2 = list2
    merged_list = None
    merged_list_ptr = merged_list
    while tmp1 is not None or tmp2 is not None:
        if tmp1 is None or (tmp2 is not None and tmp2.val < tmp1.val):
            if merged_list is None:
                merged_list = ListNode(tmp2.val)
                merged_list_ptr = merged_list
            else:
                merged_list_ptr.next = ListNode(tmp2.val)
                merged_list_ptr = merged_list_ptr.next
            tmp2 = tmp2 if tmp2 is None else tmp2.next
        else:
            if merged_list is None:
                merged_list = ListNode(tmp1.val)
                merged_list_ptr = merged_list
            else:
                merged_list_ptr.next = ListNode(tmp1.val)
                merged_list_ptr = merged_list_ptr.next
            tmp1 = tmp1 if tmp1 is None else tmp1.next
        print_list(merged_list)
    return merged_list

    
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


def merge_list_recursive(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 is None and list2 is None:
        return None

    if list1 is None or (list2 is not None and list2.val < list1.val):
        l = ListNode(list2.val)
        l.next = merge_list_recursive(list1, list2.next)
        return l
    else:
        l = ListNode(list1.val)
        l.next = merge_list_recursive(list1.next, list2)
        return l
        
def print_list(ln):
    prt = ln
    while prt is not None:
        print(prt.val, "--> ", end="")
        prt = prt.next
    print("None")
# Definition for a Linked List.


class LinkedList(object):
    list_head = None
    def __init__(self):
        pass
    def add_node(self, ln):
        pass


rand1 = random.sample(range(10),4)
rand1.sort()
rand2 = random.sample(range(10),4)
rand2.sort()

l1 = None
l2 = None 
for i in rand1:
    if l1 is None:
        l1 = ListNode(i)
        t = l1
    else:
        t.next = ListNode(i)
        t = t.next

for i in rand2:
    if l2 is None:
        l2 = ListNode(i)
        t = l2
    else:
        t.next = ListNode(i)
        t = t.next


print_list(l1)
print_list(l2)
print("Iterative: ")
print_list(merge_list_iterative(l1,l2))

t = merge_list_recursive(l1,l2)
print("Recursive: ")
print_list(t)

    