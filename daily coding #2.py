'''
ood morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!
If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!
'''

import functools
import random

def mult_except_i(lst):
    total_mult = functools.reduce(lambda x,y: x*y, lst)
    print(total_mult)
    result = [total_mult/x for x in lst]
    return result

def mult_except_i_no_div(lst):
    list_len = len(lst)
    mult_left = [None] * (len(lst) + 2)
    mult_right = [None] * (len(lst) + 2)
    mult_left[0] = mult_right[0] = 1
    mult_left[list_len+1] = mult_right[list_len+1] = 1
    result = [None] * len(lst)
    for i in range(1,list_len+1 ):
        mult_left[i] = lst[i-1] * mult_left[i-1]
    for i in range(list_len, 0, -1 ):
        mult_right[i] = lst[i-1] * mult_right[i+1]
    print(mult_left)
    print(mult_right)
    for i in range(list_len):
        result[i] = mult_left[i] * mult_right[i+2]
    return (result)


random_lst = [random.randint(1,10) for _ in range(3)]

print(random_lst)

print(mult_except_i_no_div(random_lst))