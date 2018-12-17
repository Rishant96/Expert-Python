class DistinctError(ValueError):
    """Raised when duplicate value is added to a distinctdict."""


class distinctdict(dict):
    """Dictionary that does not accept duplicate values."""
    def __setitem__(self, key, value):
        if value in self.values():
            hasKey = key in self
            if (
                (hasKey and self[key] != value) or
                not hasKey
            ):
                raise DistinctError(
                    "This value already exists for a different key"
                )
        super().__setitem__(key, value)


class Folder(list):
    def __init__(self, name):
        self.name = name

    def direc(self, nesting=0):
        offset = "  " * nesting
        print('%s%s' % (offset, self.name))

        for element in self:
            if hasattr(element, 'direc'):
                element.direc(nesting + 1)
            else:
                print("%s  %s" % (offset, element))


class Mama:
    def says(self):
        print('do your homework')


class Sister(Mama):
    def says(self):
        super().says()
        print("and clean your bedroom")


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def __repr__(self):
        return "Pizza with " + " and ".join(self.toppings)

    @classmethod
    def recommend(cls):
        """Recommend some pizza with arbitrary toppings."""
        return cls(['spam', 'ham', 'eggs'])


class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        """Use same recommendation as super but add extra spam"""
        recommended = super(VikingPizza).recommend()
        recommended.toppings += ['spam'] * 5
        return recommended


if __name__ == "__main__":
    my = distinctdict()
    my['key'] = 'value'
    # print(my)
    #  uncomment these lines to see the exception
    #  my['otherkey'] = 'value'

    # ---------------------------------------------------------------

    tree = Folder('project')
    tree.append('README.md')
    # tree.direc()

    src = Folder('src')
    src.append('script.py')
    tree.append(src)
    # tree.direc()

    # ---------------------------------------------------------------

    # Sister().says()
    # print('\n')

    anita = Sister()
    super(anita.__class__, anita).says()
    print('\n')
