'''Convert one data type to other'''

# Conversion of int to bool
# Bool of none zero is true
print(bool(0))  # False
# Rest is true
print(bool(1))
print(bool(-1))
print(bool(67))

# Conversion of float to bool
print(bool(0.0))  # False
# Rest is true
print(bool(1.0))
print(bool(-0.1))

# Convert String to bool
# bool of non-empty is true
print(bool('10'))
print(bool('hello'))
print(bool(' '))
print(bool(''))  # This is False
print(bool('True'))
print(bool('False'))  # Pay attention this is also True
print(bool(None))  # This is false

# Conversion of collection to bool
# Only empty collection is false
print(bool([]))  # Empty list is false
print(bool([1, 2, 3]))  # This is true
