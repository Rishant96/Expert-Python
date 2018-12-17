class Robot(object):
    """"Sophisticated class that moves a real robot"""
    # Don't wear down the real robots by running tests!

    def fetch(self, tool):
        print('Physical Movement! Fetching')

    def move_forward(self, tool):
        print('Physical Movement! Moving forward.')

    def move_backward(self, tool):
        print('Physical Movement! Moving backward.')

    def replace(self, tool):
        print('Physical Movement! Replacing')


class CleaningRobot(Robot):
    'Custom robot that can clean with a given tool'

    def clean(self, tool, times=10):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)


if __name__ == '__main__':
    t = CleaningRobot()
    t.clean('broom')
