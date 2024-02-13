# Here are the game riddles:

# numeric division if two numbers
level_1 = """
if variable_2 == 0:
    print("Can't divide by 0!")
else:
    print(variable_1 / variable_2)
"""
# max / min in array swap is crucial here! it will be shown in the same level
level_2 = """
min_v = max_v = table[0]
for i in range(len(table)):
    if table[i] < min_v:
        min_v = table[i]
    elif table[i] > max_v:
        max_v = table[i]
print('Max is:', max_v)
print('Min is:', min_v)
"""
# bubble short an array max / min is crucial here!
level_3 = """
n = len(table)
for i in range(n):
    for j in range(0, n - i - 1):
        if table[j] > table[j + 1]:
            table[j], table[j + 1] = table[j + 1], table[j]
print(table)
"""
# See if a substring is in a string, learn basic string manipulations with python!
level_4 = """
if string_2 in string_1:
    print('Yes!')
else:
    print('No!')
"""