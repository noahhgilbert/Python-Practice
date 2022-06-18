coin_list = [1,3,4]

def get_smallest_change(amount, coin_list):
    coins = helper(amount, coin_list)

def helper(amount, coin_list):
    if amount == 0:
        return 0
    if amount < coin_list[0]:
        return 99
    return min([1 + helper(amount - v, coin_list) for k,v in enumerate(coin_list) if amount > v])

print(get_smallest_change(57, coin_list))