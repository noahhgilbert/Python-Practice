'''
get largest sum for a contiguous subsequence of array, values can includes negatives
[1,-10,4,14,-20,11,1,-1,15,-12,4,5]
'''

import random

def max_subarray2(A):
    max_ending_here = max_so_far = A[0]
    start = stop = 0
    for e,x in enumerate(A[1:]):
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    print(max_so_far, max_ending_here, start)
    return max_so_far

def max_subarray_brute(A):
    max_sub = 0
    for i, start in enumerate(A):
        sum_curr_iter = max_curr_iter = 0
        for val in A[i:]: 
            sum_curr_iter += val
            max_curr_iter = max(max_curr_iter, sum_curr_iter)
        max_sub = max(max_sub, max_curr_iter)
    return max_sub


def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    start = stop = max_start = max_stop = 0
    for e,x in enumerate(A[1:]):
        if x > max_ending_here + x:
            max_ending_here = x
            start = e + 1
        else: 
            max_ending_here += x
            stop = e + 1
        #max_ending_here = max(x, max_ending_here + x)
        if max_so_far < max_ending_here:
            max_start = start
            max_stop = stop

        max_so_far = max(max_so_far, max_ending_here)

    print(max_so_far, max_ending_here, A[max_start:max_stop+1])
    return max_so_far

ran_list = [random.randint(-15,15) for _ in range(10)]
print(ran_list)
print(max_subarray(ran_list))
print(max_subarray_brute(ran_list))


'''
   
'''