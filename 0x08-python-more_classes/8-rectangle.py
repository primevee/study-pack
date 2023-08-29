#!/usr/bin/python3
"""
    This is a empty class called rectangle
"""


class Rectangle:
    """
        This is an empty class
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Initializes a rectangle instance

            Args:
                width (int): width of rectangle
                height (int): height of rectangle
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
            A method for str

            Returns:
                str: A string representaing of a parimeter

        """
        self.prem = ""
        for _ in range(self.height):
            self.prem += str(self.print_symbol) * self.width + '\n'
        return self.prem.strip()

    def __repr__(self):
        """
            A method that prints a string representation of instances

            Returns:
                str: string representation of instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
            A method for deleting an instance

            Returns:
                None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
            Getter method for width of rectangle

            Returns:
                int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter for width of rectangle

            Args:
                value (int): width of rectangle

            Raises:
                TypeError: If value is not integer
                ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Getter method for height of rectangle

            Returns:
                int: Value of height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter method for height of a rectangle

            Args:
                value (int): height of rectangle

            Raises:
                TypeError: If value is not integer
                ValueError: If value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Area method that returns the area

            Returns:
                int: width * height
        """

        return self.width * self.height

    def perimeter(self):
        """
            Area method that returns perimeter

            Returns:
                int: 2 * (height + width)
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            A static method to compare rectangle sizes

            Args:
                rect_1 (Rectangle): rectangle 1
                rect_2 (Rectangle): rectangle 2

            Returns:
                rect_1 if rect_1 is bigger or equal to rect_2 else rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
