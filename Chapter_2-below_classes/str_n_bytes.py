"""
 Strings in Python are sequences.
 However, They are different from other container types
 in that they have a limitation on what data they can store,
 namely, Unicode Text.
"""

sample_str = "Hello World"

byte_str = bytes([102, 111, 11])
print(list(byte_str))

name, designation = "Rishant", "Mr."
print(f'Hello, {designation} {name}')

print('It is good to see you too, {} {}'.format("Ms.", "Nora"))

str_msg = f'Hello, {name} {designation}. ₹'
byte_msg = str_msg.encode()

print(byte_msg.decode())

substrings = ('abc', 'xyz', 'sub', 'string')
s = ""
for substr in substrings:
    s += substr
print(s)

s_2 = ",".join(substrings)
print(s_2)
print("Hello", "World")
