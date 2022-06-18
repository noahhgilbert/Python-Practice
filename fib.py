import timeit

def fib_iterative(n):
    n_minus_1 = 1
    n_minus_2 = 1
    #total = 0
    total = 1
    if n == 0:
        return 0
    elif n <= 3:
        return 1
    else:
        for i in range(4,n+1):
            #print(f'n_minus_1 {n_minus_1} n_minus_2 {n_minus_2} total {total}')
            #total = n_minus_1 + n_minus_2
            total += n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = total
            #print(f'n_minus_1 {n_minus_1} n_minus_2 {n_minus_2} total {total}')
    return total

def fib_recursive(n):
    if n == 0:
        return 0
    if n <= 3:
         return 1
    #print(f'n is {n}')
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_recursive_dynamic(n, mem):
    if str(n) in mem:
        return mem[str(n)]
    if n == 0:
        return 0
    if n <= 3:
         return 1
    print(f'n is {n}')
    mem[str(n)] = fib_recursive_dynamic(n-1,mem) + fib_recursive_dynamic(n-2,mem)
    return mem[str(n)]

#print(fib_iterative(8))

#for i in range(8):
#    print(fib_recursive(i))

#print(fib_recursive_dynamic(8,{}))
iterative = timeit.Timer(stmt = "fib_iterative(15)", setup = "import fib")
recursive = timeit.Timer(stmt = "fib_recursive(15)", setup = "import fib")
dynamic = timeit.Timer(stmt = "fib_recursive_dynamic(15,{})", setup = "import fib")
print(f'Iterative {iterative.timeit(5)} \n Recursive {recursive.timeit(5)} \n Dynamic {dynamic.timeit(5)}')