
# print(dir(tuple()), "\n")
# print(dir(list()))

"""
Python Idioms for lists
"""


"""
 1 - Python list 'Comprehension'
"""

evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
print(f'using c style for loop,\n{evens}\n')

# ----------------------------------------------

evens = [i for i in range(10) if i % 2 == 0]
print(f'using python comprehension,\n{evens}\n')


"""
 2 - Usiing the built-in function 'enumerate'
"""

print("Using old school counter variable 'i',\n")
i = 0
for element in ['one', 'two', 'three']:
    print(i, element)
    i += 1
print("\n")

# ----------------------------------------------

print("Getting the count using the 'enumerate' function,\n")
for i, element in enumerate(['one', 'two', 'three']):
    print(i, element)
print("\n")


"""
 3 - Using 'zip' to aggregate elements from multiple lists
"""
print("Showcasing 'zip',")
for item in zip([1, 2, 3], [4, 5, 6]):
    print(item)
print('\n')

print("Reversing 'zip',")
for item in zip(*zip([1, 2, 3], [4, 5, 6])):
    print(item)
print("\n")

"""
 4 - Sequence unpacking
"""
first, second, third = "foo", "bar", 100
print(first)
print(second)
print(third)
print("\n")

# Unpacking allows you to capture multiple elements in a single expression
# using starred expressions, as long as it can be interpreted unambiguosly

first, second, *rest = 0, 1, 2, 3
print(first)
print(second)
print(rest)
print("\n")

# starred expresiion to capture middle of the sequence
first, *inner, last = 0, 1, 2, 3
print(first)
print(inner)
print(last)
print("\n")

# nested unpacking
(a, b), (c, d) = (1, 2), (3, 4)
print(a, b, c, d)
