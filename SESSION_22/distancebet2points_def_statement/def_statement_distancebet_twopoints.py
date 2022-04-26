"""
@author: Ganesh Jadhawar
@goal: to calculate distance between to two points whose co-ordinates are given using def statement
"""


def distance_for(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    :param x1: x co-ordinate for point1
    :param y1: y co-ordinate for point1
    :param x2: x co-ordinate for point2
    :param y2: y co-ordinate for point2
    :return: distance calculated between (x1,y1) and (x2,y2)
    """
    if type(x1) != int and type(x1) != float :
        print("Co-ordinate given for x1 of point 1 are not valid")
        return None
    if type(y1) != int and type(y1) != float :
        print("Co-ordinate given for y1 of point 1 are not valid")
        return None
    if type(x2) != int and type(x2) != float :
        print("Co-ordinate given for x2 of point 2 are not valid")
        return None
    if type(y2) != int and type(y2) != float :
        print("Co-ordinate given for y2 of point 2 are not valid")
        return None

    d = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return d


res = distance_for(4, 5, 10, 20)

print(res)

