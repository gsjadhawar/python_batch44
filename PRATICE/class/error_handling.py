

def factorial(n):
    if type(n) != int:
        raise TypeError("bad type for n is passed")

    if n == 0 or n == 1:
        return 1

    if n < 0:
        raise ValueError("negative value passed to factorial")

    rs = n * factorial(n-1)
    return rs


def main():
    try:
        n = -11
        rs = factorial(n)
        print("factorial of", n, "is:", rs)
    except TypeError as e:
        print("type(e):", type(e))
        print("Error:", e.args[0])

    except ValueError as e:
       print("Error is:", e.args[0])

    print("continuing the code")
main()
