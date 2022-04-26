"""
@author: Ganesh
@goal: to calculate gravitational force between two objects
"""

def gravitational_force(m1: float, m2: float, d: float) -> float:
    """
    to calculate gravitational force between two m1 and m2 objects.
    :param m1: mass of the object1
    :param m2: mass of the object2
    :param d: distance between object1 and object2
    :return: calculated gravitational force between two objects
    """
    if type(m1) != int and type(m1) != float:
        print("value provided for m1 is not valid type")
        return None

    if type(m2) != int and type(m2) != float:
        print("value provided for m2 is not valid type ")
        return None

    if type(d) != int and type(d) != float:
        print("value provided for d is not valid type")
        return None

    G = 6.67 * (10 ** -11)
    F = (G * m1 * m2) / (d ** 2)

    return F


force = gravitational_force(10, 5, 2)

print("Force between objects is:", force)

help(gravitational_force)