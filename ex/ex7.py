def trace1 (fn):
    """Return a version of fn that first print it is called"""
    def trace(x):
        print('调用',fn, '参数',x)
        return fn(x)
    return trace

@trace1
def square(x):
    return x*x
@trace1
def sum_to_square(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k+1
    return total