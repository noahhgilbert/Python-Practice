


def merge(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1


    if list1.val <= list2.val:
        
        tmp = list1.next
        list1.next = merge(tmp, list2)
        return (list1)
    else:
        tmp = list2.next
        list2.next = merge(list1, tmp)
        return (list2)

# Definition for a Linked List.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(6)


b = ListNode(2)
b.next = ListNode(9)
b.next.next = ListNode(11)

merged = merge(a,b)



while merged  != None:
    print("->" + str(merged.val))
    merged = merged.next

