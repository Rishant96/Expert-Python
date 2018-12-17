from contextlib import contextmanager
from threading import RLock
lock = RLock()


def synchronized(function):
    def _synchronized(*args, **kwargs):
        lock.acquire()
        try:
            return function(*args, **kwargs)
        finally:
            lock.release()
        return _synchronized


@synchronized
def thread_safe():  # make sure it locks the response
    pass

# Context managers - the 'with' statement


"""
 try...finally can be in many places, such as:
    1 - Closing a file
    2 - Releasing a lock
    3 - Making a temporary code patch
    4 - Running protected code in a special environment
"""

"""
 'with' statement factors out these use cases by providing a simple
 way to wrap a block of code
"""
# Eg. 1 - Working with a file

#   Using try...finally

hosts = open('/etc/hosts')
try:
    for line in hosts:
        if line.startswith('#'):
            continue
        print(line.strip())
finally:
    hosts.close()

#   Using 'with' statement

with open('/etc/hosts') as hosts:
    for line in hosts:
        if line.startswith('#'):
            continue
        print(line.strip())

# Context managers - As a class

class ContextIllustration:
    def __enter__(self):
        print("entering context")

    def __exit__(self, exec_type, exec_value, traceback):
        print('leaving context')

        if exec_type is None:
            print('with no error')
        else:
            print('with an error (%s)' % exec_value)


@contextmanager
def context_illustration():
    print('entering context')

    try:
        yield
    except Exception as e:
        print('leaving context')
        print('with an error (%s)' % e)
        # exception needs to be reraised
        raise
    else:
        print('leaving context')
        print('with no error')
