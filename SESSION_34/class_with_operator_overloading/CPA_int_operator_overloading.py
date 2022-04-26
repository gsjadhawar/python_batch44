"""
@author: Yogeshwar
@goal:  To demonstrate operator overloading of ALU operations with the help of
        wrapper integer class
"""


class CPA_int:

    def __init__(self, init_n: int):
        print("In CPA_int.__init__")
        self.n = init_n

    def __add__(self, other):
        """
        Accept two CPA_int objects in self and other.
        :param other: CPA_int object
        :return: Third CPA_int object which is a summation object of self and other
        """
        print("CPA_int.__add__")
        n_sum: int = self.n + other.n
        cn_sum: CPA_int = CPA_int(n_sum)
        return cn_sum

    def __sub__(self, other):
        """
        Accept two CPA_int objects in self and other
        :param other: CPA_int object
        :return: third CPA_int object which is a subtraction of self and other
        """
        print("CPA_int.__sub__")
        n_sub = self.n - other.n
        cn_sub = CPA_int(n_sub)
        return cn_sub

    def __mul__(self, other):
        """

        :param other: CPA_int object
        :return: third CPA_int object which is a multiplication of self and other
        """
        print("CPA_int.__mul__")
        n_mul = self.n * other.n
        cn_mul = CPA_int(n_mul)
        return cn_mul

    def __floordiv__(self, other):
        """

        :param other: CPA_int object
        :return: a third CPA_int object which is a quotient object when self is divided by other
        """
        print("In CPA_int.__floordiv__:(QUOTIENT):")
        q = self.n // other.n
        cn_q = CPA_int(q)
        return (cn_q)

    def __mod__(self, other):
        """

        :param other: CPA_int object
        :return: a third CPA_int object which is a remainder object when self is divided by other
        """
        print("In CPA_int.__mod__:(REMAINDER)")
        r = self.n % other.n
        cn_r = CPA_int(r)
        return cn_r

    def __truediv__(self, other):
        """

        :param other: CPA_int object
        :return: a floating point object which is a true division of integers inside self and other
        """
        print("In CPA_int.__truediv__:(FLOATING POINT DIVISION):")
        return self.n / other.n

    def __pow__(self, power):
        """

        :param power: CPA_int object
        :return: returns third CPA_int object which is a exponential operation object (self ** other)
        """
        print("In CPA_int.__pow__(To compute a ** b):")
        n_pow = self.n ** power.n
        cn_pow = CPA_int(n_pow)
        return cn_pow

    def __lt__(self, other):
        print("In CPA_int.__lt__:(less than)")
        b = (self.n < other.n)
        return b

    def __le__(self, other):
        print("In CPA_int.__le__(less than or equal to)")
        b = (self.n <= other.n)
        return b

    def __gt__(self, other):
        print("In CPA_int.__gt__(greater than)")
        b = (self.n > other.n)
        return b

    def __ge__(self, other):
        print("In CPA_int.__ge__(greater than or equal to)")
        b = (self.n >= other.n)
        return b

    def __eq__(self, other):
        print("In CPA_int.__eq__(equal to)")
        b = (self.n == other.n)
        return b

    def __ne__(self, other):
        print("In CPA_int.__ne__(not equal to)")
        b = (self.n != other.n)
        return b

    def show(self, msg) -> None:
        print(msg, self.n)



cn1 = CPA_int(10)
cn2 = CPA_int(3)

cn_sum = cn1 + cn2
cn_sum.show("Addition by Operator:")
print("type(cn1):", type(cn1))
print("type(cn2):", type(cn2))
print("type(cn_sum):", type(cn_sum))

cn_sub = cn1 - cn2
cn_sub.show("Subtraction by operator:")

cn_mul = cn1 * cn2
cn_mul.show("Multiplication by operator:")

cn_q = cn1 // cn2
cn_q.show("Quotient by Operator:")

cn_r = cn1 % cn2
cn_r.show("Remainder by operator:")

f_div = cn1 / cn2
print("type(f_div):", type(f_div))
print("f_div:", f_div)

cn_exp = cn1 ** cn2
cn_exp.show("Exponential operation by operator:")

if cn1 < cn2:
    print("cn1 < cn2 == True")
else:
    print("cn1 < cn2 == False")

if cn1 <= cn2:
    print("cn1 <= cn2 == True")
else:
    print("cn1 <= cn2 == False")

if cn1 > cn2:
    print("cn1 > cn2 == True")
else:
    print("cn1 > cn2" == False)

if cn1 >= cn2:
    print("cn1 >= cn2")

if cn1 == cn2:
    print("cn1 == cn2")

if cn1 != cn2:
    print("cn1 != cn2")

"""
<=      __le__
>       __gt__
>=      __ge__
==      __eq__ 
!=      __ne__ 
"""
