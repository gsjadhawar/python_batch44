
import sys

class Point2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class triangle():
    def __init__(self, tup_a, tup_b, tup_c):
        len_AB = ((tup_a[0] - tup_b[0]) ** 2 + (tup_a[1] - tup_b[1]) ** 2) ** 0.5
        len_BC = ((tup_b[0] - tup_c[0]) ** 2 + (tup_b[1] - tup_c[1]) ** 2) ** 0.5
        len_CA = ((tup_c[0] - tup_a[0]) ** 2 + (tup_c[1] - tup_a[1]) ** 2) ** 0.5

        if (len_AB + len_BC <= len_CA) or (len_BC + len_CA <= len_AB) or (len_AB + len_CA <= len_BC):
            print("parameters passed can't form triangle")
            sys.exit(-1)

        self.A = Point2D(tup_a[0], tup_a[1])
        self.B = Point2D(tup_b[0], tup_b[1])
        self.C = Point2D(tup_c[0], tup_c[1])

        self.AB = len_AB
        self.BC = len_BC
        self.CA = len_CA

    def getAB(self):
        return self.AB

    def getBC(self):
        return self.BC

    def getCA(self):
        return self.CA


T1 = triangle((0, 0), (10, 10), (0, 10))

print("print lenght of AB:", T1.getAB())


