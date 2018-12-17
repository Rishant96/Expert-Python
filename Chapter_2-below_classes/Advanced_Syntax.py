# Iterators

"""
 An iterator is nothing more than a container object that implements
 the iterator protcol. It is based on two methods:
    1 - __next__: This returns the next item of the container
    2 - __iter__: This returns the iterator itself
"""

i = iter('abc')
print(next(i))
print(next(i))
print(next(i))

# Creating a custom iterable class


class CountDown:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """"Return the next element."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """Return the iterator itself."""
        return self


print('\n')
for element in CountDown(4):
    print(element)

# Using 'yield' to create Generators -  Eg. Fibonacci series


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def one_to_ten():
    for i in range(1, 11):
        yield i

fib = fibonacci()
print('\n')
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

print([next(fib) for i in range(10)])

print("\n")
nums = one_to_ten()
print(nums)
for i in range(15):
    try:
        print(next(nums))
    except StopIteration:
        break

# More on Generators
print('\n')


def power(values):
    for value in values:
        print('powering %s' % value)
        yield value


def adder(values):
    for value in values:
        print("adding to %s" % value)
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2


elements = [1, 4, 7, 9, 12, 19]
results = adder(power(elements))
print(next(results))
print(next(results))
print(next(results))

# more powerful generators


def psychologist():
    print('Please tell me your problems')
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too many questions")
            elif 'good' in answer:
                print("Ahh that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negative")
