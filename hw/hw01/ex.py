"""our first Python source file"""

from operator import floordiv, mod

def divide_exact(n,d):
   """Return the quotient and remainder of dividing N by D.

   >>> q, r = divide_exact(2021,10)
   >>> q
   202
   >>> r
   1
   """ 
   return floordiv(n,d), mod(n,d)

#    lecture 2
def prime_factors(n):
    """Print the prime factors of n in the form
    
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(13)
    13
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_prime_factors(n)
        n = n // k
        print(k)
def smallest_prime_factors(n):
    k = 2
    while n%k != 0:
        k = k+1
    return k