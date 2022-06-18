def reversal(input_stinrg):
    string_to_reverse = list(input_stinrg)
    print(string_to_reverse)
    end = len(string_to_reverse)
    print(end)
    start = 0
      
    while start < end:
        tmp = string_to_reverse[start]
        string_to_reverse[start] = string_to_reverse[end- 1]
        string_to_reverse[end-1] = tmp
        start += 1
        end -= 1
    print(string_to_reverse)

def reversal_recursive(inpu_string):
    print(inpu_string)
    end = len(inpu_string)
    if len(inpu_string) <= 1:
        return inpu_string
    #t = list(inpu_string)
    return inpu_string[end -1] + reversal_recursive(inpu_string[1:end-1]) +  inpu_string[0]

print(reversal_recursive("abcdefg"))