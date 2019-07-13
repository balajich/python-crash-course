''' While loops
Move to the starting of loop with out executing below statemetn
'''
# print from 0 to 10, skipping 5
i = 0
while i <= 10:
    if i == 5:
        i = i + 1
        continue  # The control will jump to starting of the loop
    print(i)
    i = i + 1
