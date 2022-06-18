blocks = [
{
    "a":False, #
    "b":True,
    "c":False
}
,
{
    "a":True,
    "b":True,
    "c":False
}
,
{
    "a":False,
    "b":True,
    "c":False
}
,
{
    "a":False,
    "b":False,
    "c":False
}
,
{
    "a":False,
    "b":False,
    "c":False
}
,
{
    "a":False,
    "b":False,
    "c":True
}
]


reqs = ["a","b","c"]




def get_best_block(blocks, reqs):
    req_dict = {}
    for req in reqs:
        req_dict[req] = 99
    print(req_dict)
    dist = [None for i in range(len(blocks))]
    for i in range(len(blocks)):
        dist[i] = req_dict.copy()
        pass
    for i in range(len(blocks)):
        for req in reqs:
            if blocks[i][req]:
                dist[i][req] = 0
            elif i > 0:
                if dist[i-1][req]==99:
                    dist[i][req]=99
                else:
                    dist[i][req] = dist[i-1][req] + 1
    print(dist)
    apt_index = len(blocks) - 1
    apt_best_distance = 99
    for i in range(len(blocks)-1,-1,-1):
        apt_distance = 0
        for req in reqs:
            if blocks[i][req]:
                dist[i][req] = 0
            elif i < len(blocks) - 1:
                if dist[i+1][req]==99:
                    dist[i][req] = min(99,dist[i][req])
                else:
                    dist[i][req] = min(dist[i+1][req] + 1, dist[i][req])
            apt_distance += dist[i][req]
        if apt_best_distance > apt_distance:
            apt_index = i
            apt_best_distance = apt_distance
    
    #blocks[i-1][print(f"{i}{blocks[i]}")

    print(dist)
    print(f"Best apartment is at {apt_index} with distance {apt_best_distance} from all requirements")

get_best_block(blocks, reqs)

