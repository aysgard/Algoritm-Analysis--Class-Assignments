
### Q3.2

import unittest
from ex3 import Node, LinkedList

class TestLinkedListBubbleSort(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def linked_list_from_array(self, arr):
        for num in arr:
            self.ll.addLast(num)
        return self.ll

    def testcase_a(self):
        input_data = [1, 4, 67, 100, 250, 300, 280, 130, 90, 80, 10, -5]
        expected_output = sorted(input_data)

        my_linked_list = self.linked_list_from_array(input_data).LinkedListBubbleSort()

        self.assertEqual(my_linked_list.to_list(), expected_output)
        print(f"Test Case a Results: {my_linked_list.to_list()}")

    def testcase_b(self):
        input_data = [3, 2, 1, 5, 9, 0]
        expected_output = [0, 1, 2, 3, 5, 9]

        my_linked_list = self.linked_list_from_array(input_data).LinkedListBubbleSort()

        self.assertEqual(my_linked_list.to_list(), expected_output)
        print(f"Test Case b Results: {my_linked_list.to_list()}")

if __name__ == '__main__':
    unittest.main()
