lst = [1 ,2, 4, 4]
target = 9

def find_sum(lst, target):
    idx1 = 0
    idx2 = len(lst) - 1
    while idx1 < idx2:
        tmp_sum = lst[idx1] + lst[idx2]
        if tmp_sum == target:
            return [idx1, idx2]
        if tmp_sum > target:
            idx2 -= 1
        else:
            idx1 += 1
    return [-1,-1]

print(find_sum(lst, target))