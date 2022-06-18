import random
from functools import reduce

full_set = [random.randint(1,100) for x in range(10)]
remove_index = random.randint(0,9)
partial_set = full_set[:remove_index] + full_set[remove_index+1:]
print(full_set)
print(partial_set)
#print(full_set.append(partial_set))
complete_set = full_set + partial_set
print(complete_set)
missing = reduce(lambda x,y: x^y , complete_set)
print(missing)