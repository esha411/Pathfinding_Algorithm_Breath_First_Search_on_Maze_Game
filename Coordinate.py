class Coordinate:

    def __init__ (self, y: int, x: int, parent):
        self.y = y
        self.x = x
        self.parent = parent

        if self.parent is not None:
            self.count = parent.count + 1
        else:
            self.count = 0
