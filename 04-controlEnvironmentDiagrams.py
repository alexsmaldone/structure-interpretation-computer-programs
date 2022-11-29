def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x


def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining


def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0


# ================================
# Environment for NEsted Definitions
# ================================

def make_adder(n):
    def adder(k):
        return k + n
    return adder

def triple(x):
    return 3 * x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

"""
interative env example:

squadder = compose1(square, triple)
-- then call squadder(5) or any number
OR
compose1(square, make_adder(2))(3)
 = 25
"""
