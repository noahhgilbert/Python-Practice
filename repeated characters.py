string = "alfkalf aldfnkdnlsdflekr kb;lsm;lsm;gm"

d = {}


[]

for a in string:
    print(a)
    if a in d:
        d[a] = d[a] + 1
    else:
        d[a] = 1


[print(x,y) for x,y in d.items() if y > 1]