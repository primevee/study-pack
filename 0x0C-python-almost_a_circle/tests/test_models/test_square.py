#!/usr/bin/python3
"""
"""


from models.square import Square
import unittest
from io import StringIO
import sys


class Test_Square(unittest.TestCase):
    """
    """

    def test_square_creation(self):
        """
        """

        s1 = Square(5, 0, 0, 1)
        self.assertEqual(s1.area(), 25, "Area should be 25")

        stored_val = StringIO()
        sys.stdout = stored_val

        print(s1)

        actual_out = stored_val.getvalue().strip()
        self.assertEqual(actual_out, "[Square] (1) 0/0 - 5")
        s1.size = 2
        self.assertEqual(s1.size, 2)
        stored_val.truncate(0)
        stored_val.seek(0)

        s1.display()
        sys.stdouot = sys.__stdout__
        actual_out = stored_val.getvalue().strip()
        self.assertEqual(actual_out, "##\n##")

        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_update(self):
        """
            Test update method
        """

        s1 = Square(5)
        s1.update(10)

        stored_val = StringIO()
        sys.stdout = stored_val

        print(s1)

        sys.stdout = sys.__stdout__
        actual_out = stored_val.getvalue().strip()
        self.assertEqual(actual_out, "[Square] (10) 0/0 - 5")

        s1.update(size=7, y=1)
        stored_val = StringIO()
        sys.stdout = stored_val

        print(s1)
        sys.stdout = sys.__stdout__
        actual_out = stored_val.getvalue().strip()
        self.assertEqual(actual_out, "[Square] (10) 0/1 - 7")


if __name__ == "__main__":
    unittest.main()
