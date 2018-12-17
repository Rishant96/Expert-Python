import unittest
from robot import Robot, CleaningRobot


class MockBot(Robot):
    """Simulates a real robot by simply recording tasks"""

    def __init__(self):
        self.tasks = []

    def fetch(self, tool):
        self.tasks.append(f'fetching {tool}')

    def move_forward(self, tool):
        self.tasks.append(f'forward {tool}')

    def move_backward(self, tool):
        self.tasks.append(f'backward {tool}')

    def replace(self, tool):
        self.tasks.append(f'replace {tool}')


class MockedCleaningRobot(CleaningRobot, MockBot):
    'Inject a mock bot into the robot dependency'
    pass


class TestCleaningRobot(unittest.TestCase):
    def test_clean(self):
        t = MockedCleaningRobot()
        t.clean('mop')
        expected = (['fetching mop'] +
                    ['forward mop', 'backward mop'] * 10 +
                    ['replace mop'])
        self.assertEqual(t.tasks, expected)


if __name__ == '__main__':
    unittest.main()
