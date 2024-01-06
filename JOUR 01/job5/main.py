class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f'Point: ({self.x}, {self.y})')

    def afficherX(self):
        print('x:', self.x)

    def afficherY(self):
        print('y:', self.y)

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y


point = Point(2, 3)


point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(5)
point.changerY(6)
point.afficherLesPoints()