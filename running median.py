'''
get running median in a stream of numbers
'''

import math

def get_child_index(parent_index):


def print_median(balance, not_a_heap):
    if balance == 0:
        returne not_a_heap[0]
    
math.ceil


def get_median(lst):
    not_a_heap = [None] * len(2^math.ceil(math.log(lst,2)))
    not_a_heap[0] = lst[0]
    balance = 0
    for num in lst[1:]:
        if num <= not_a_heap[0]:
            if balance >= -1:
                add_left(num, not_a_heap)
            balance -= 1
        else:
            add_right(num, not_a_heap)
            balance += 1
        print_median(balance, not_a_heap)

    
