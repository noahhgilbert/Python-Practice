'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

# number may start with 1 or 2
# number may only be length 1 or 2
# if number starts with 2 and next number is 6 or lower then may be two options
#create an array of 26 - actually do i need letters?  really ust eed to ensure that the count is correct, 

def decode(num_list):
    if len(num_list) == 1:
        #print(char_list[num_list[0] - 1])
        return 1
    if len(num_list) == 2:
        #print(char_list[num_list[0] - 1], char_list[num_list[1] - 1])
        if num_list[1] <= 6:
            #print(char_list[num_list[0] * 10 + num_list[1] - 1])
            return 2
        else:           
            return 1
    return decode(num_list[1:]) + decode(num_list[2:])

def decode2(num_list):
    if len(num_list) == 1:
        #print(char_list[num_list[0] - 1])
        return char_list[num_list[0] - 1]
    if len(num_list) == 2:
        #print(char_list[num_list[0] - 1], char_list[num_list[1] - 1])
        if num_list[1] <= 6:
            return (char_list[num_list[0] - 1] + char_list[num_list[1] - 1])
            #print(char_list[num_list[0] * 10 + num_list[1] - 1])
            return 2
        else:           
            return 1
    return decode(num_list[1:]) + decode(num_list[2:])


char_list = [chr(i+97) for i in range(26)]

print (char_list)

print(decode([1,1,1,1]))