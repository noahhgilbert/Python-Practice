lst = [2,4,6,7,9,10,16]
target = 16

def get_number_of_subsets(num_list, targ,mem):
    mem_key = str(num_list[0]) + "--" + str(targ)
    if (mem_key) in mem:
        return mem[mem_key]
    if num_list[0] > targ:
        return 0
    if num_list[0] == targ:
        return 1
    if len(num_list) == 1:
        return 0
    num_including_num_list0 = get_number_of_subsets(num_list[1:], targ-num_list[0],mem)
    num_excluding_num_list0 = get_number_of_subsets(num_list[1:], targ,mem)
    mem[mem_key] = num_including_num_list0 + num_excluding_num_list0
    return  mem[mem_key]

print(get_number_of_subsets(lst, target,{}))
