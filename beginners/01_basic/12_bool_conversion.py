'''Convert one data type to other'''

# Convert String to int
print(int('10'))

# Convert String to float
print(float('10.2'))

# Convert String to bool
# bool of non-empty is true
print(bool('10'))
print(bool('hello'))
print(bool(' '))
print(bool(''))  # This is False
print(bool('True'))
print(bool('False'))  # Pay attention this is also True
print(bool(None))  # This is false
