import sys


class wrap_int():
    def __init__(self, num):
        if type(num) != int:
            print("parameter passed is of invalid type")
            sys.exit(-1)
        self.value = num

    def add(self, other):
        """
        #Note: type(self) --> wrap_int, type(other) --> wrap_int
        #type(self.value) --> int, type(other.value) --> int
        #type(summation) --> int
        #type(result) --> wrap_init
        #self.value = 10
        #self.other = 20
        #result.value = 30
        """
        summation = self.value + other.value
        result = wrap_int(summation)
        return result

    def sub(self, other):
        subtraction = self.value - other.value
        result = wrap_int(subtraction)
        return result

    def mul(self, other):
        multiplication = self.value * other.value
        result = wrap_int(multiplication)
        return result

    def quo(self, other):
        quotient = self.value // other.value
        result = wrap_int(quotient)
        return result

    def remain(self, other):
        remainder = self.value % other.value
        result = wrap_int(remainder)
        return result

    def show(self, msg):
        print(msg, self.value)


n = wrap_int(10)
print("type(n):", type(n))
print("dict in n is:", n.__dict__)

m = wrap_int(20)
print("type(m):", type(m))
print(" m is:", m.__dict__['value'])

summation = m.add(n)
subtraction = m.sub(n)
multiplication = m.mul(n)
quotient = m.quo(n)
remainder = m.remain(n)

m.show("m =")
summation.show("summation =")
subtraction.show("subtraction =")
multiplication.show("multiplication =")
quotient.show("quotient =")
remainder.show("remainder =")