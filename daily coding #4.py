'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

[3 1 5 4 9]



You can modify the input array in-place.

Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!
'''

import random

def get_first_missing_int(lst):
    for i,v in enumerate(lst):
        print (i)
        while lst[i] != i+1:
            if lst[i] < 1:
                break
            if lst[i] > len(lst):
                break
            if lst[lst[i]-1] == lst[i]:
                break
            lst[lst[i]-1],lst[i] = lst[i],lst[lst[i]-1]
        print(lst)
    
    for i,v in enumerate(lst):
        if i + 1 != v:
            return i+1

randarray = [random.randint(-1,7) for _ in range(5)]
print(randarray)
print(get_first_missing_int(randarray))