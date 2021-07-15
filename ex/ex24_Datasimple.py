def min_abs_indices(s):
    """Indices of all elements in list s themselves the smallest absolute value
    
    >>> min_abs_indices([-4,-3,-2,3,2,4])
    [2,4]
    >>> min_abs_indices([1,2,3,4,5])
    [0]
    """
    min_abs = min(map(abs,s)) # 这个例子里面min_abs=2
    # [x for x in s if abs(x) == min_abs] # [-2, 2]
    return [i for i in range(len(s)) if abs(s[i]) == min_abs] # [2,4]
    # 解法2
    # f = lambda i: abs(s[i]) == min_abs
    # filter(f,range(len(s)))
    # return list(filter)
def largest_adj_sum(s):
    """ Largest sum of two adjacent elements in a list s.
    
    >>> largest_adj_sum([-4,-3,-2,3,2,4])
    6
    >>> largest_adj_sum([-4,-3,-2,-3,2,-4])
    1
    """
    max(s[i]+s[i+1] for i in range(len(s) - 1))
    # 解法2 奇淫巧计 
    # list(zip(s,s)) >>> [(-4,-4),(-3,-3),(-2,-2),(3,3),(2,2),(4,4)]
    # list(zip(s[:-1],s[1:])) >>> [(-4,-3),(-3,-2),(-2,3),(3,2),(2,4)] 正好每个错开1位,每个元组就是相邻元素对
    # return max([a + b for a, b in zip(s[:-1],s[1:])])

def digit_dict(s):
    """ Map each digit d to the lists of elements in s that end with d

    >>> digit_dict([5,8,13,21,34,55,89])
    {1:[21],3:[13],4:[34],5:[5,55],8:[8],9:[89]}
    """
    # 奇淫巧计
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}
    # 正常模式
    # last_digits = [x % 10 for x in s]
    # {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digits}
def all_have_an_equal(s):
    """ Does every element equal some other element in S?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    # i = 1
    # s[i] >>> 3
    # s[:i] >>> [4]
    # s[i+1:] >>> [2,3,2,4]
    # s[:i] + s[i+1:] >>> [4,2,3,2,4]
    # s[i] in s[:i] + s[i+1:] >>> True
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])
    # 解法2
    # [y for y in s if y == 3] >>> [3,3]
    # [1 for y in s if y ==3 ] >>> [1,1]
    # sum ([1 for y in s if y == 3]) >>> 2
    # [sum([1 for y in s if y == x]) for x in s] >>> [2,2,2,2,2,2]
    # all([sum([1 for y in s if y == x]) for x in s]) >>> True
    # min([sum([1 for y in s if y == x]) for x in s]) >>> 2
    # min([sum([1 for y in s if y == x]) for x in s]) > 1 >>> True
    # s.count(3) >>> 1
    # min([s.count(x) for x in s]) >>> 2
    # min([s.count(x) for x in s]) > 1 >>> True

# 链表类练习
class Link:
    """ A linked list
    >>> Link(1, Link(2, Link(3))
    Link(1,Link(2, Link(3)))
    >>> s = Link(1, Link(Link(2, Link(3)),Link(4)))
    >>> s
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(s)
    <1 <2 3> 4>
    """
    empty = ()

    def __init__(self, first, rest = empty):
        assert rest is Link.empty or instance(rest, Link)
        self.first = first
        self. rest = rest
    
    def __repr__(self):
        if self.rest:
            rest_repr = ', '+ repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
        
def ordered(s):
    """ Is Link s ordered? 
    >>> ordered(Link(1,Link(3, Link(4))))
    True
    >>> ordered(Link(1, Link(4, Link(3))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))))
    False
    >>> ordered(Link(1, Link(-3, Link(4))), key = abs)
    True
    >>> ordered(Link(1, Link(4, Link(3))), key = abs)
    False
    """

def merge(s,t):
    """ Return a sorted Link with the elements of sorted s & t
    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a,b)
    Link(1, Link(1, Link(4,Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))

    """

def merge_in_place(s, t):
    """ Return a sorted Link with the elements of sorted s & t
    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge_in_place(a,b)
    Link(1, Link(4, Link(5)))
    >>> a
    