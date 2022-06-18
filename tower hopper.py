import random


def is_hoppable(tower_list):
    #print("Jumping from {}".format(tower_list[0]))
    if tower_list[0] > len(tower_list) - 1:
        #print("Jumped from {} to success {} - {}".format(tower_list[0], tower_list, len(tower_list)))
        return True
    elif tower_list[0] == 0:
        #print("Failed hop")
        return False
    else:
        return any([is_hoppable(tower_list[x + 1:]) for x in range(tower_list[0])])

def is_hoppable2(tower_list):
    max_index = tower_list[0] - 1
    cur_index = 0
    while cur_index <= max_index:
        if tower_list[cur_index] + cur_index >= len(tower_list):
            return True 
        if tower_list[cur_index] + cur_index > max_index:
            max_index = tower_list[cur_index] + cur_index
        cur_index += 1
    return False

for _ in range(10):
    towers = [random.randint(0,3) for _ in range(6)]
    print(towers, is_hoppable2(towers))