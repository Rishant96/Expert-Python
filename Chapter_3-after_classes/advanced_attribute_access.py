# Name mangling
class MyClass:
    __secret = 'my_secret'

# descriptors


if __name__ == '__main__':
    instance_of = MyClass()
    # print(instance_of._MyClass__secret)
