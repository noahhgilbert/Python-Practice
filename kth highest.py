import heapq
test_array = [1,4,5,2,19,6,6,13,8]

def kth_highest(k, arry):
    firstk = arry[:k]
    heapq.heapify(firstk)
    
    for i in range(k, len(arry)):
        minval = heapq.heappop(firstk)
        if arry[i] > minval:
            heapq.heappush(firstk, arry[i])
        else:
            heapq.heappush(firstk, minval)

    return heapq.heappop(firstk)


print(kth_highest(7, test_array))

