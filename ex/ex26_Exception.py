from operator import add, mul
#
# 方法1
# def reduce(f, s, initial):
#     """ Combine elements of s using f starting at

#     >>> reduce(mul, [2, 4, 8], 1)
#     64
#     >>> reduce(add, [1, 2, 3, 4], 0)
#     10
#     """
#     for x in s:
#         initial = f(initial, x)
#     return initial

def reduce(f, s, initial):
    """ Combine elements of s

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """ 
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))
