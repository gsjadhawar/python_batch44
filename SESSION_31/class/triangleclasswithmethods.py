"""
@authors: Ganesh Jadhawar
@goals: to implement triangle class with methods
"""
import sys


class Point2D:
    """
    Implementation of class two dimensional point cartesian co-ordinate system
    """

    def __init__(self, x: int, y: int):
        """
        constructor of Point2D class
        :param x: value of x co-ordinate
        :param y: value of y co-ordinate
        """
        if type(x) != int and type(x) != float:
            print("Invalid data type given to actual parameter x")
            sys.exit(-1)
        if type(y) != int and type(y) != float:
            print("Invalid data type given to actual parameter y")
            sys.exit(-1)

        self.x = x
        self.y = y

    def get_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


def type_check_triangle_parameter(v) -> bool:
    if type(v) != tuple:
        return False
    if len(v) != 2:
        return False
    if (type(v[0]) != int and type(v[0]) != float) or (type(v[1]) != int and type(v[1]) != float):
        return False
    return True


class triangle:
    def __init__(self, init_vertex_a: tuple, init_vertex_b: tuple, init_vertex_c: tuple):
        if (type_check_triangle_parameter(init_vertex_a) == False) or (type_check_triangle_parameter(init_vertex_b) == False) or (type_check_triangle_parameter(init_vertex_c) == False):
            print("invalid data type passed to triangle class")
            sys.exit(-1)

        self.vertex_a = Point2D(init_vertex_a[0], init_vertex_a[1])
        self.vertex_b = Point2D(init_vertex_b[0], init_vertex_b[1])
        self.vertex_c = Point2D(init_vertex_c[0], init_vertex_c[1])

        self.len_ab = self.vertex_a.get_distance(self.vertex_b)
        self.len_bc = self.vertex_b.get_distance(self.vertex_c)
        self.len_ca = self.vertex_c.get_distance(self.vertex_a)

    def perimeter(self):
        return self.len_ab + self.len_bc + self.len_ca

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.len_ab) * (s - self.len_bc) * (s - self.len_ca)) ** 0.5

