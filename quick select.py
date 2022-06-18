import random
import math

def quick_sort(arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        pivot = partition(arr,left,right)
        quick_sort(arr[left:pivot])
        quick_sort(arr[pivot+1:right])
    return arr
        


def partition(arr, left, right):
    print("Partitioning {arr} from {left} to {right}".format(arr=arr,left=left,right=right))
    partition_index = left
    pivot = arr[partition_index]
    left += 1
    while left < right:
        while arr[left] < pivot and left < right:
            left += 1
            print("Left: {left}".format(left=left))
        while arr[right] > pivot and right >= left:
            right -= 1
            print("Right: {right}".format(right=right))
        if arr[left] > arr[right]:
            print("Swapping {left} with {right}".format(left = arr[left], right=arr[right]))
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[partition_index], arr[left] = arr[left], arr[partition_index]
    print("Partitioned {arr} from {left} to {right}".format(arr=arr,left=left,right=right))
    return partition_index

num_array = [random.randint(1,100) for _ in range(8)]
print(num_array)
print(quick_sort(num_array))