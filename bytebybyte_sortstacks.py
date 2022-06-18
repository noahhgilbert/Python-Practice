#bytebybyte_Sort Stacks
'''
Given a stack, sort the elements in teh stack using no more than  on additional stack
'''
list = [1,54,67,3,2,56,1,6]
stack = []
sorted_stack=[]
for i in list:
    stack.append(i)

print(stack)
print(stack.pop())
print(stack)

def sort_stack(stack, sorted_stack):
    for i in range(len(stack)):
        sorted_stack = place_value(sorted_stack, stack.pop())
    return sorted_stack



def place_value(sorted_stack, val):
    if len(sorted_stack) == 0:
        sorted_stack.append(val)
        return sorted_stack
    tmp = sorted_stack.pop()
    if val >= tmp:
        sorted_stack.append(tmp)
        sorted_stack.append(val)
        return sorted_stack
    a = place_value(sorted_stack, val)
    a.append(tmp)
    return a

print(sort_stack(stack, sorted_stack))