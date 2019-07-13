''' While loops
while expr:
    print("loop while expr is True")
expr is converted to bool using bool() constructor
'''
# print from 0 to 10
i = 0
while i <= 10:
    print(i)
    i = i + 1

# print from 10 to 1
i = 10
while i:
    print(i)
    i = i - 1
