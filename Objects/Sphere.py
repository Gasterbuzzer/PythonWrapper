""" Sphere Object Representation """

from Objects.Color import Color


class Sphere:
    """
    Class Representing a Sphere
    """

    def __init__(self, position=None, radius=1.0, color=None, index=1, parent=None, translation=None, rotation=None,
                 scaling=None) -> None:
        """
        Class representing a Sphere Object.
        :param position: (X, y, z) Example: [0, 0, 0]
        :param radius: Radius of Sphere
        :param color: Color Object
        :param index: (int) Index of Sphere.
        :param parent: Parent of Object.
        """

        if color is None:
            color = Color()
        if position is None:
            position = [0, 0, 0]
        if radius is None:
            radius = 1.0
        if index is None:
            index = 1

        self.position = position
        self.radius = radius
        self.color = color
        self.index = index
        self.parent = parent

        # Special Attributes
        self.translation = translation
        self.rotation = rotation
        self.scaling = scaling

    def check_if_default(self, variable, name) -> bool:
        """
        Checks if a given parameter of a sphere is a default value.
        :param variable: (Example: self . position) Must be a variable in sphere.
        :param name: Name/Variable Name of the variable to check.
        :return: True if default and false if not.
        """
        print(f"Debug Log: {self} is checking for {name} if default.")

        if name == "position":
            if variable == [0, 0, 0]:
                return True
            else:
                return False

        elif name == "radius":
            if variable == 1.0:
                return True
            else:
                return False

        elif name == "index":
            if variable == 1:
                return True
            else:
                return False

        elif name == "parent":
            if variable is None:
                return True
            else:
                return False

        elif name == "color":
            if variable == Color():
                return True
            else:
                return False

        elif name == "translation":
            if variable == [0, 0, 0]:
                return True
            else:
                return False

        elif name == "rotation":
            if variable == [0, 0]:
                return True
            else:
                return False

        elif name == "scaling":
            if variable == [0, 0, 0]:
                return True
            else:
                return False

        else:
            print(f"Medium Error: Cannot recognize {name} if it is part of the object.")
            return False
