def permute(s, list):
    if s == 1:
        return list
    else:
        return [ y + x
                 for y in permute(1, list)
                 for x in permute(s - 1, list)
                 ]

print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b"]))
print(permute(3, ["a","b"]))