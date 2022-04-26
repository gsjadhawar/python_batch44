"""
@author: Ganesh Shankar Jadhawar
@goal: to Implement Triangle class and implement methods to get perimeter, area of triangle.
"""

import sys


class Point2D:
    def __init__(self, x: int, y: int):
        """
        :param x: x co-ordinate of point
        :param y: y co-ordinate of point
        """
        type_check_list = [int, float]
        if type(x) not in type_check_list:
            print("bad data type passed for Point2D class parameter")
            sys.exit(-1)

        type_check_list = [int, float]
        if type(y) not in type_check_list:
            print("bad data type passed for Point2D class parameters")
            sys.exit(-1)

        self.x = x
        self.y = y


class triangle:
    def __init__(self, init_vertex_a: tuple, init_vertex_b: tuple, init_vertex_c: tuple):
        """
        :param init_vertex_a: co-ordinates for point A as tuple
        :param init_vertex_b: co-ordinates for point B as tuple
        :param init_vertex_c: co-ordinates for Point C as tuple
        """
        if type(init_vertex_a) != tuple or type(init_vertex_b) != tuple or type(init_vertex_c) != tuple:
            print("bad data type for parameter of triangle class")

        len_ab = ((init_vertex_a[0] - init_vertex_b[0]) ** 2 + (init_vertex_a[1] - init_vertex_b[1]) ** 2) ** 0.5
        len_bc = ((init_vertex_b[0] - init_vertex_c[0]) ** 2 + (init_vertex_b[1] - init_vertex_c[1]) ** 2) ** 0.5
        len_ac = ((init_vertex_a[0] - init_vertex_c[0]) ** 2 + (init_vertex_a[1] - init_vertex_c[1]) ** 2) ** 0.5

        if len_ab + len_bc < len_ac or len_bc + len_ac < len_ab or len_ab + len_ac < len_bc:
            print("vertexes passed do not form triangle")
            sys.exit(-1)
        peri = (len_ab + len_bc + len_ac)
        semi = peri / 2
        self.vertex_a = Point2D(init_vertex_a[0], init_vertex_a[1])
        self.vertex_b = Point2D(init_vertex_b[0], init_vertex_b[1])
        self.vertex_c = Point2D(init_vertex_c[0], init_vertex_c[1])

        self.len_ab = len_ab
        self.len_bc = len_bc
        self.len_ac = len_ac
        self.peri = peri
        self.semi = semi

    def perimeter(self) -> float:
        return self.peri

    def area(self) -> float:
        result = (self.semi*(self.semi - self.len_ab) * (self.semi - self.len_bc) * (self.semi - self.len_ac)) ** 0.5
        return result

    def show(self, msg) -> None:
        print(msg, self.__dict__)

T1 = triangle((0, 0), (0, 2), (3, 0))
P = T1.perimeter()
A = T1.area()
T1.show("co-ordinate are")
print("perimeter is:", P)
print("area is:", A)
