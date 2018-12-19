# Name mangling
class MyClass:
    __secret = 'my_secret'

# descriptors - lets you customize attribute access logic


"""
    Descritpor Protocol:

        1. __set__(self, obj, type=None): 'setter'
        2. __get__(self, obj, value): 'getter'
        3. __delete__(self, obj): called when 'del' is invoked
                                 on the attribute.

    * A descriptor that implements __get__() and __set__()
      is called 'data descriptor'

    * A descriptor that just implements __get__(), is called
      a 'non-data descriptor'
"""


class RevealAccess():
    """
     A data descriptor that sets and returns values
     normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self .val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val


class MyDescClass:
    x = RevealAccess(10, 'var "x"')
    y = 5


if __name__ == '__main__':
    instance_of = MyClass()
    # print(instance_of._MyClass__secret)

    m = MyDescClass()
    print(m.x)
    m.x = 20
    print(m.x)
    print(m.y)
