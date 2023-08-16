"""Color Representation of Objects"""


class Color:
    """
    Color Representation
    """

    def __init__(self, ambient=None, diffuse=None, specular=None, reflected=None, refracted=None, shininess=1) -> None:
        """
        Class Representing Color for an Object.
        :param ambient: Ambient of the Object.
        :param diffuse: Diffuse of the Object.
        :param specular: Specular of the Object.
        :param reflected: Reflected of the Object.
        :param refracted: Refracted from the Object.
        :param shininess: (Int) Shininess of the Object.
        """

        self.default_value_list = [0, 0, 0]
        self.default_value_shininess = 1

        # Default Values
        if refracted is None:
            refracted = [0, 0, 0]
        if reflected is None:
            reflected = [0, 0, 0]
        if specular is None:
            specular = [0, 0, 0]
        if diffuse is None:
            diffuse = [0, 0, 0]
        if ambient is None:
            ambient = [0, 0, 0]
        if shininess is None:
            shininess = self.default_value_shininess

        # Saving Values
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflected = reflected
        self.refracted = refracted
        self.shininess = shininess

    def check_if_default(self, variable) -> bool:
        """
        Checks if a given parameter of a sphere is a default value.
        :param variable: (Example: self . position) Must be a variable in sphere.
        :return: True if default and false if not.
        """

        if variable is self.ambient:
            if variable == self.default_value_list:
                return True
            else:
                return False

        elif variable is self.diffuse:
            if variable == self.default_value_list:
                return True
            else:
                return False

        elif variable is self.specular:
            if variable == self.default_value_list:
                return True
            else:
                return False

        elif variable is self.reflected:
            if variable == self.default_value_list:
                return True
            else:
                return False

        elif variable is self.refracted:
            if variable == self.default_value_list:
                return True
            else:
                return False

        elif variable is self.shininess:
            if variable == self.default_value_shininess:
                return True
            else:
                return False

        else:
            return False
