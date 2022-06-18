unflattened = {"a":"b","c":{"d":"e","f":"g","h":{"i":"j","k":"l"},"m":"n"},"o":"p"}

def flatten_json(j):
    flattened_json = {}
    for k,v in j.items():
        if type(v) is dict:
            flattened_tmp = flatten_json(v)
            for k_1, v_1 in flattened_tmp.items():
                flattened_json[k + "_" + k_1] = v_1
            print(flattened_json)
        else:
            flattened_json[k] = v
            print(flattened_json)
        #print("Key: {k}, Value {v} (Type: {t}".format(k=k, v=v, t=type(v)))
    return(flattened_json)

print(flatten_json(unflattened))