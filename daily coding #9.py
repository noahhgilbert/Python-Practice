'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!
'''
import random

#if first of pair is larger, take it and move forward two spaces.  OR if both of pair are <= 0 move forward two spaces
# if second of pair is larger

#[1 2 3 4 5 6 100] 109
#[1 2 3 9 5 6 100] 111 
#[1 3 100 1000 10000]
#[1 3 100 1000 5 100000]

rand_list = [random.randint(0,20) for _ in range(10)]
print(rand_list)

def get_largest_non_adj_sum(lst):
    mem = [None] * len(lst)
    mem[0] = max(lst[0],0)
    mem[1] = max(lst[1],lst[0],0)
    max_sum = 0
    for i in range(2, len(lst)):
        max_sum = max(max(lst[i],0) + mem[i-2], mem[i-1], 0)
        mem[i] = max_sum
        print(mem)
    return max_sum
'''
    sum = 0
    while i < len(lst):
        if lst[i] <= 0 and lst[i+1] <=0:
            i += 2
        else if lst[i] > lst[i+1]:
            sum += lst[i]
            i += 2
        else:


        if lst[i] > 
    for val in lst:
        if val <= 0:
            continue
        print(val)
'''
print(get_largest_non_adj_sum(rand_list))