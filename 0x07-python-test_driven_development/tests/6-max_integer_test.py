import unittest
max_integer = __import__('6-max_integer').max_integer
"""
    This module contains unit test for max_integer

    The max_integer finds the max in a list

"""


class TestMaxInteger(unittest.TestCase):

    """
        Test class for max_integer

    """

    def test_max_integer(self):

        """
        Test cases for max_integer

        Each test case checks to see that the correct max is \
                computed by function
        """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 2, -3, -4, 0]), 2)


if __name__ == '__main__':
    unittest.main()
