'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!
'''
import random
import time

def get_pair(lst):
    for k,n1 in enumerate(lst):
        for n2 in lst[k+1:]:
            if n1 + n2 == 100000:
                return n1,n2
    return 0



def get_pair_opt(lst):
    ht = {}
    for n in lst:
        if (100000 - n) in ht:
            return n, 100000-n
        ht[n] = 1
    return 0

nums = [random.randint(0,99999) for _ in range(1000)]
start_time = time.time()
print("Unoptimized get_pair(nums) returned {ret_values} in {secs} seconds".format(ret_values=get_pair(nums), secs = time.time() - start_time))
start_time = time.time()
print("Optimized get_pair_opt(nums) returned {ret_values} in {secs} seconds".format(ret_values=get_pair_opt(nums), secs = time.time() - start_time))