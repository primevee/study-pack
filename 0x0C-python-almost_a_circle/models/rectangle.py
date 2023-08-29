#!/usr/bin/python3
"""
    the modules has a Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
        The rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            class initialisation

            Args:
                width (int, float): width
                height (int, float): height
                x (int, float): x
                y (int, float): y
                id (int): id

        """

        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        if width < 1:
            raise ValueError("width must be > 0")
        if x < 0:
            raise ValueError("x must >= 0")
        if y < 0:
            raise ValueError("y must >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def to_dictionary(self):
        """
            Returns a dictionary
        """

        return {"x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width}

    def update(self, *args, **kwargs):
        """
            update the instance
        """

        if args:
            num_args = len(args)
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.width = args[1]
            if num_args > 2:
                self.height = args[2]
            if num_args > 3:
                self.x = args[3]
            if num_args > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """
            prints in stdout the Rectangle instance with the character #
        """

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def area(self):
        """
            returns the area of a square
        """

        return self.__width * self.__height

    @property
    def width(self):
        """
            this gets the value of the width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
            this sets width to value
        """

        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            this gets the value of the height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            this sets height to value
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
            this gets the value of the x
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
            this sets x to value
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
            this gets the value of the x
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
            this sets y to value
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
