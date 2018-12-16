dict_1 = {
            1: 'one',
            2: 'two',
            3: 'three'
        }
# print(dict_1)

# Dictionary Comprehension

# squares = {number: number ** 2 for number in range(100)}
# print(f'\n{squares.keys().__class__}\n{dir(squares.keys())}\n')

"""
 In python, dictinaries do not preserve the order in which the keys
 were added.
"""

# It might preserve for integers because of how their
# hash values are calculated
print({number: None for number in range(5)}.keys())

print({str(number): None for number in range(5)}.keys())

print({str(number): None for number in reversed(range(5))}.keys())
