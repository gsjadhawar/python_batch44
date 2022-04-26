"""
@author: Ganesh Jadhawar
@goal: To implement vector class along with methods to get magnitude of vector, angle of vector.
"""

import math
import sys


class vector:
    def __init__(self, head_x: float, head_y: float):
        """
        This is class constructor.
        :param head_x: x co-ordinate of vector's head
        :param head_y: y co-ordinate of vector's head
        """
        type_check_list = [float, int]
        if type(head_x) not in type_check_list:
            print("bad data type for vector")
            sys.exit(-1)

        if type(head_y) not in type_check_list:
            print("bad data type for vector")
            sys.exit(-1)

        self.x = head_x
        self.y = head_y

    def get_length(self) -> float:
        """
        This method is to get length of vector
        :return: it returns float value
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_angle(self) -> float:
        """
        This method return the angle of given vector object
        :return: returns angle as float value
        """
        return math.atan(self.y / self.x)

    def __add__(self, other):
        """
        This method return summation of two vectors.
        :param other: this is another vector object
        :return: returns vector object which is sum of two given vector objects
        """
        summation_x = self.x + other.x
        summation_y = self.y + other.y
        v_sum = vector(summation_x, summation_y)
        return v_sum

    def __sub__(self, other):
        """
        This method is used to get subtraction between two vectors.
        :param other: is another vector object
        :return: returns vector object
        """
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        v_sub = vector(sub_x, sub_y)
        return v_sub

    def __mul__(self, other) -> float:
        """
        This method is to get multiplication or dot of two vectors
        :param other: is another vector object
        :return: returns result as float.
        """
        dot = self.x * other.x + self.y * other.y
        return dot

    def __str__(self):
        return str(self.__dict__)

v1 = vector(2.2, 4.5)
v2 = vector(3.5, 5.5)
length = v1.get_length()
angle = v1.get_angle()
'''
summation = v1.addition(v2)
subtraction = v1.subtraction(v2)
mul = v1.dot(v2)
print("summation of v1 & v2 vector is:", summation.__dict__)
print("subtraction of v1 & v2 vector is:", subtraction.__dict__)
print("dot product of v1 & v2 vector is:", mul)
'''
v_add = v1 + v2
v_sub = v1 - v2
v_dot = v1 * v2

print("length of the vector:", v1, "is", length)
print("angle of the vector:", v1, "is", angle)
print("addition of v1 & v2 is:", v_add)
print("subtraction of v1 & v2 is:", v_sub)
print("multiplication of v1 & v2:", v_dot)
