input_lst="abcdefg" * 100000
occurence_lst = [[] for i in range(26)]
for index in range(len(input_lst)):
    occurence_lst[ord(input_lst[index]) - 97].append(index)

print(occurence_lst)


