""" Half-Space Object Representation """

from Objects.Color import Color


class HalfSpace:
    """
    Class Representing a Half Space
    """

    def __init__(self, position=None, normal=None, color=None, index=1) -> None:

        # It would perhaps be better if we made a parent class representing HalfSpace and Sphere.

        if normal is None:
            normal = [1, 0, 0]
        if color is None:
            color = Color()
        if position is None:
            position = [0, 0, 0]

        self.position = position
        self.normal = normal
        self.color = color
        self.index = index
