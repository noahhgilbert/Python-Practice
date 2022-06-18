import os
#print(os.path.realpath())

def fizz_buzz(n, div):

    for i in range(n):
        out = ""
        for d in div:
            if i % d[0] == 0:
                out += d[1]
        out = i if out == "" else out
        print(out)

fizz_buzz(61,[(3,"fizz"),(5,"buzz"),(4,"chirp")])