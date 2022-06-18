def recursive_fib(n):
    if n == 1 or n==2:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)

call_count = 0
def dynamic_fib_help(n, memo):
    call_count += 1
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n==2:
        return 1
    memo[n] = recursive_fib(n-1) + recursive_fib(n-2)
    return memo[n]

def dynamic_fib(n): 
    return dynamic_fib_help(n, [None]*(n+1))

print(recursive_fib(7))
print([dynamic_fib(x) for x in range(1,10)])
#1 1 2 3 5 8 13