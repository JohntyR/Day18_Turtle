class Shape:
    def __init__(self, sides, colour):
        self.sides = sides
        self.angle = 360 / self.sides
        self.colour = colour
