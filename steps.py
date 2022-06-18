steps = [1,3,5]

def get_unique_paths(n, steps):
    memo = [None] * (n + 1)
    memo[0] = 1
    return get_unique_paths_helper(n,steps,memo)


def get_unique_paths_helper2(n, steps, memo):
    print("called")
    if n == 0:
        return 1
    if n < 0:
        return 0
    sum = 0
    for step in steps:
        sum += get_unique_paths(n-step, steps)
    #return get_unique_paths(n-1) + get_unique_paths(n-2)
    return sum

def get_unique_paths_helper(n, steps, memo):
    print(f"called {n}")
    if n < 0:
        return 0
    if memo[n] is not None:
        print (f"returned cached {memo[n]} for {n}")
        return memo[n]
    sum = 0
    #for i in range(1,n+1):
    for step in steps:
        #print(n,i,step)
        sum += get_unique_paths_helper(n-step, steps, memo)
    memo[n] = sum
        #print(sum)
    return sum  

print(get_unique_paths(100, steps))