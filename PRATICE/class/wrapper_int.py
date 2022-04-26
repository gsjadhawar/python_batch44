"""
@author: Ganesh Jadhawar
@goal: To implement wrapper class for int data type.
"""
import sys


class wrap_int:
    def __init__(self, n: int):
        """
        This is constructor for wrap_int class
        :param n: this is int value for object
        """
        if type(n) != int:
            print("bad type for wrap_int")
            sys.exit(-1)
        self.n = n

    def __str__(self) -> str:
        return str(self.n)

    def __add__(self, other):
        addition = self.n + other.n
        return wrap_int(addition)

    def __sub__(self, other):
        sub = self.n - other.n
        return wrap_int(sub)

    def __mul__(self, other):
        mul = self.n * other.n
        return wrap_int(mul)

    def __mod__(self, other):
        mod = self.n % other.n
        return wrap_int(mod)

    def __floordiv__(self, other):
        div = self.n // other.n
        return wrap_int(div)

    def __truediv__(self, other):
        real_div = self.n / other.n
        return real_div

    def __pow__(self, other):
        result = self.n ** other.n
        return wrap_int(result)

    def __lt__(self, other):
        if self.n < other.n:
            return True
        else:
            return False

    def __le__(self, other):
        if self.n <= other.n:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.n > other.n:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.n >= other.n:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.n == other.n:
            return True
        else:
            return False


n1 = wrap_int(10)
n2 = wrap_int(5)

print("summation is:", n1 + n2)
print("subtraction is:", n1 - n2)
print("multiplication is:", n1 * n2)
print("modulus is:", n1 % n2)
print("floordiv is:", n1 // n2)
print("real division is:", n1 / n2)
print("power is:", n1 ** n2)
result = n1 > n2
print(result)
print(n1 <= n2)
