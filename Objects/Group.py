""" Group Object Representation """


class Group:
    """
    Class Representing a Group of Objects
    """

    def __init__(self, objects=None, parent=None, translation=None, rotation=None, scaling=None) -> None:
        """
        Class representing a Group of Objects.

        :param parent: Parent of Object.
        """

        if objects is None:
            objects = []

        self.objects = objects
        self.parent = parent

        # Special Attributes
        self.translation = translation
        self.rotation = rotation
        self.scaling = scaling

        # Very special attribute
        self.special = "union"

    def check_if_default(self, variable) -> bool:
        """
        Checks if a given parameter of a sphere is a default value.
        :param variable: (Example: self . position) Must be a variable in sphere.
        :return: True if default and false if not.
        """

        if variable is self.translation:
            if variable is None:
                return True
            else:
                return False

        elif variable is self.rotation:
            if variable is None:
                return True
            else:
                return False

        elif variable is self.scaling:
            if variable is None:
                return True
            else:
                return False

        else:
            return False
