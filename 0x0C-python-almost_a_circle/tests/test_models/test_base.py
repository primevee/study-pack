#!/usr/bin/python3
"""
 base class unit test
"""


import unittest
from models.base import Base


class Test_base(unittest.TestCase):
    """
    """

    def test_base_id(self):
        """
        """

        base_1 = Base(12)
        self.assertEqual(base_1.id, 12, "Id value should be 12")
        base_2 = Base()
        self.assertEqual(base_2.id, 1, "Base should be equal to 1")
        base_3 = Base()
        self.assertEqual(base_3.id, 2, "Base should be equal to 2")
        base_4 = Base()
        self.assertEqual(base_4.id, 3, "Base should be equal to 3")
        base_5 = Base(254)
        self.assertEqual(base_5.id, 254, "Base should be equal to 254")
        base_6 = Base()
        self.assertEqual(base_6.id, 4, "Base should be equal to 4")


if __name__ == "__main__":
    unittest.main()
