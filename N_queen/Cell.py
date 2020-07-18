class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.free = True
        self.queen = False
        self.tried = 0

    def chosen_queen(self):
        self.free = False
        self.queen = True
