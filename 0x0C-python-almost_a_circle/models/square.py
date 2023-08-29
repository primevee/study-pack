#!/usr/bin/python3
"""
    This module has the square class it inherits from the rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        This is the Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            initialising the Square class
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            change __str__ function
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    def to_dictionary(self):
        """
             returns dict representation
        """

        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y}

    def update(self, *args, **kwargs):
        """
            updates the Square instance
        """

        if args:
            args_len = len(args)
            if args_len > 0:
                self.id = args[0]
            if args_len > 1:
                self.size = args[1]
            if args_len > 2:
                self.x = args[2]
            if args_len > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def size(self):
        """
            size getter
        """

        return self.width

    @size.setter
    def size(self, value):
        """
            this sets the value of width and height
        """

        self.width = value
        self.height = value
