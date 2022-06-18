coin_list = coinsOptions = [1,5,10,25,100]

coin_list = coinsOptions = [1,2,5]
t = 5

def dynamic(target, coins):
    ways = [1]+[0]*target
    for coin in coins:
        for i in range(coin,target+1):
            ways[i]+=ways[i-coin]
    #print (ways)
    return (ways[target])

def recursive_wrapper(target, coins):
    def recursive(target,index):
        print(target, " - ", index)
        if target < 0:
            #print (str(coins[index]) + " + 0")
            return 0
        if target == 0:
            print (str(coins[index]) + " + 1***********")
            return 1
        return sum([recursive(target - c, i) for i, c in enumerate(coins[index:])])
    return recursive(target, 0)


def recursive_wrapper2(target, coins):
    def recursive(target,index):
        print(target, " - ", index)
        if target < 0:
            #print (str(coins[index]) + " + 0")
            return 0
        if target == 0:
            print (str(coins[index]) + " + 1***********")
            return 1
        combos = 0
        for i in range(index,len(coins)):
            combos += recursive(target - coins[i], i)
        return combos
    return recursive(target, 0)

def numberOfWays(target):
    if (target < 0):
        return 0
    elif(target == 0):
        return 1
    else:
        return sum([numberOfWays(target - coin) for coin in coinsOptions])

print (numberOfWays(t))

print(dynamic(t, coin_list))

print(recursive_wrapper2(t, coin_list))

