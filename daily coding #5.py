'''Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car1(f):
    def left(a, b):
        return a
    return f(left)

def car(pair):
    return(pair(lambda x,y: x))

def cdr(pair):
    return(pair(lambda x,y: y))

def cdr2(f):
    def right(a, b):
        return b
    return f(right)

print(car(cons(3,4)))
print(cdr(cons(3,4)))