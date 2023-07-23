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

        # Default Values
        if refracted is None:
            refracted = [1, 1, 1]
        if reflected is None:
            reflected = [1, 1, 1]
        if specular is None:
            specular = [1, 1, 1]
        if diffuse is None:
            diffuse = [1, 1, 1]
        if ambient is None:
            ambient = [1, 1, 1]

        # Saving Values
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflected = reflected
        self.refracted = refracted
        self.shininess = shininess
