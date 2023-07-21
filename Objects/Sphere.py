""" Sphere Object Representation """

from Objects.Color import Color


class Sphere:
    """
    Class Representing a Sphere
    """

    def __init__(self, position=None, radius=1.0, color=None, index=1) -> None:

        if color is None:
            color = Color()
        if position is None:
            position = [0, 0, 0]

        self.position = position
        self.radius = radius
        self.color = color
        self.index = index
