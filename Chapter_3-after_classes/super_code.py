# 1 - mixing 'super' and explicit class calls


class A:
    def __init__(self):
        print("A", end=" ")
        super().__init__()


class B:
    def __init__(self):
        print("B", end=" ")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C", end=" ")
        # A.__init__(self)
        # B.__init__(self)
        super().__init__()


# 2 - Heterogenous arguments

class CommonBase:
    def __init__(self):
        print('CommonBase')
        super().__init__()


class Base1(CommonBase):
    def __init__(self):
        print('Basel')
        super().__init__()


class Base2(CommonBase):
    def __init__(self):
        print('Base2')
        super().__init__()


class MyClass(Base1, Base2):
    def __init__(self, arg):
        print('my base')
        super().__init__(arg)


if __name__ == '__main__':
    # C()

    # -----------------------------------------------------

    MyClass()