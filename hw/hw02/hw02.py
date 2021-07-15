HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x == 0:
        return 0
    if x%10 == 8:
        return num_eights(x//10)+1
    else:
        return num_eights(x//10)
        


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def helper(index, ppn, dir):
        if index == n:
            return ppn
        elif num_eights(index)!=0 or index%8==0:
            return helper(index + 1, ppn-dir, -dir)
        else:
            return helper(index + 1, ppn+dir , dir)
    return helper(1,1,1)

    # index, ppn, dir = 1,1,1
    # while index != n:
    #     index += 1
    #     ppn += dir
    #     if num_eights(index) != 0 or index % 8 ==0:
    #         dir = -dir
    # return ppn


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    # missing_digits(1248) -> 4 (3,5,6,7)
    # missing_digits(124) -> 1 (3)
    # (124) -> 1 而(1248)->4 差别就是倒数第一位数和倒数第二位数 8-4-1 = 3
    # 特殊情况
    # missing_digits(1122) -> 0
    # missing_digits(112) -> 0 
    # 这种情况 都是0 同时 (2-2-1 =-1)  < 0
    if (n//10 == 0):
        return 0
    lastdight = n%10    # 倒数第一位数
    secondlastdight = (n//10) %10 # 倒数第二位数
    missing = lastdight - secondlastdight - 1
    if(missing <0):
        missing = 0
    return missing_digits(n//10) + missing


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    def ways(smallest_coin,remain_coins):
        # number of ways of make change for remain_coins such that 最小的钱数 >= smallest_coin
        if not smallest_coin:
            # note that: next_largest_coin(25) = None
            return 0
        elif smallest_coin > remain_coins:
            return 0
        elif smallest_coin == remain_coins:
            return 1
        
        next_smallest = next_largest_coin(smallest_coin)
        """
        用不少于smallest coin 的钱分 remain coins 的方法数=
        当前方法至少存在一个零钱等于smallest coin的方法数+
        当前方法不存在任意一个零钱等于smallest coin(即用不少于next smallest的钱分 remains coins)的方法数
        """
        return ways(smallest_coin, remain_coins-smallest_coin) + ways(next_smallest, remain_coins)
    return ways(1,total)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda a: lambda v: a(a, v))(lambda s, x: 1 if x == 1 else x*s(s, x-1))

