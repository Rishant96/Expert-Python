from collections import Counter, OrderedDict
"""
 Somewhat redundant, as of python 3.7
 because standard dictionaries in python are now ordered
"""

# Using 'super' to create OrderedCounters


class OrderedCounter(Counter, OrderedDict):
    """Counter that remembers the order elements are first seen in"""
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__,
                           OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


oc = OrderedCounter('abracadara')
print(oc)
