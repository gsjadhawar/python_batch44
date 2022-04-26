import sys


class quadrilateral:
    def __init__(self, a, b, c, d):
        """
        :param init_a: first side of quadrilateral
        :param init_b: second side of quadrilateral
        :param init_c: third side of quadrilateral
        :param init_d: fourth side of quadrilateral
        """
        valid_type = [int, float]

        if type(a) not in valid_type or type(b) not in valid_type or type(c) not in valid_type or type(d) not in valid_type:
            print("bad data type for sides are passed")
            sys.exit(-1)

        if a + b + c < d or a + b+ d < c or b + c + d < a or c + d + a < b:
            print("passed sides can not create the quadrilateral")
            sys.exit(-1)

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        """
        :return: the area of calling object
        """
        sp = self.perimeter() / 2
        return ((sp - self.a) * (sp - self.b) * (sp - self.c) * (sp - self.d)) * 0.5

    def perimeter(self):
        """
        :return: the perimeter of calling object
        """
        return self.a + self.b + self.c + self.d


class square(quadrilateral):
    def __init__(self, side):
        valid_type = [int, float]
        if type(side) not in valid_type:
            print("side has invalid data type")
            sys.exit(-1)

        self.side = side
        quadrilateral.__init__(self, side, side, side, side)

    def get_diagonal(self):
        """
        :return:  the length of diagonal of calling object
        """
        return self.side * (2 ** 0.5)

x = square(5.5)
print("area of square is:", x.area())
print("length of diagonal of square is", x.get_diagonal())

