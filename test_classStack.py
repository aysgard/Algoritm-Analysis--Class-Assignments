
### Q2.2

import unittest
from classStack import Stack

class TestStackOperations(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_findMin(self):

        numbers = [3, -2, 1, 5, 9, 0]
        for num in numbers:
            self.stack.push(num)    # bottom: 3 top: 0

        expected_min = -2
        actual_min = self.stack.findMin()

        self.assertEqual(actual_min, expected_min)
        print(f"min: {actual_min}")
        self.assertEqual(self.stack.getSize(), 6)
        print(f"size: {self.stack.getSize()}")

    def test_reverse(self):

        numbers = [3, -2, 1, 5, 9, 0]
        for num in numbers:
            self.stack.push(num)

        reversed_stack = self.stack.reverse() # should be [0, 9, 5, 1, -2, 3] (Bottom -> Top)

        expected_pop_order = [3, -2, 1, 5, 9, 0]

        for expected_value in expected_pop_order:
            popped_value = reversed_stack.pop()
            self.assertEqual(popped_value, expected_value)
            print(f"popped: {popped_value}")

        self.assertTrue(reversed_stack.isEmpty())


if __name__ == '__main__':
    unittest.main()

