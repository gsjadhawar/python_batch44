

class triangle:
    def __init__(self, init_point1: list, init_point2: list, init_point3: list):
        self.point1 = init_point1
        self.point2 = init_point2
        self.point3 = init_point3


triangle1 = triangle([1, 2], [2, 3], [4, 5])

print("printing triangle co-ordinates:", triangle1.__dict__)


class circle:
    def __init__(self, init_radius: int, init_centre: list):
        self.radius = init_radius
        self.centre = init_centre


circle1 = circle(5, [2, 2])

print("printing circle details:", circle1.__dict__)


class complex_num:
