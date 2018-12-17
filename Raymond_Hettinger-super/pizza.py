class DoughFactory(object):

    def get_dough(self):
        return "insecticide treated wheat dough"


class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        print('Getting dough')

        # Bad design - DoughFactory is hardcoded
        dough = DoughFactory().get_dough()

        # Good Design - super is automatically aware of any changes
        dough = super().get_dough()

        print(f'Making pie with {dough}')
        for topping in toppings:
            print(f'Adding: {topping}')


if __name__ == '__main__':
    Pizza().order_pizza('Pepperoni', 'Bell Pepper')
    help(Pizza)
