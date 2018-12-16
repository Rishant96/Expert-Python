class WithoutDecorators:
    def some_static_method():
        pass  # print("this is a static method")
    some_static_method = staticmethod(some_static_method)

    def some_class_method(cls):
        pass  # print("this is a class method")
    some_class_method = classmethod(some_class_method)


class WithDecorators:
    @staticmethod
    def some_static_method():
        pass  # print("this is a static method")

    @classmethod
    def some_class_method(cls):
        pass  # print("this is a class method")


# Decorators - As a function

def mydecorator(function):
    def wrapped(*args, **kwargs):
        # do some stuff before the original
        # function gets called
        result = function(*args, **kwargs)
        # do some stuff after the function call
        # and return the result
        return result
    # return the wrapper as a decorated function
    return wrapped


# Decorators - As a class

class DecoratorAsClass:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # do some stuff before the original
        # functon gets called
        result = self.function(*args, **kwargs)
        # do some stuff after function call and
        # return the result
        return result


# Parameterizing decorators

def repeat(number=3):
    """
     Cause decorated function to be repeated a number of times.

     Last value of original function call is returned as a result
     :param number: number of repititions, 3 if not specified
    """
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
                return result
            return wrapper
        return actual_decorator
