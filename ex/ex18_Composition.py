class Link:

    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

square = lambda x: x*x
odd = lambda x: x%2 ==1

def range_link(start, end):
    """
    >>> range_link(3,6)
    Link(3,Link(4,Link(5)))
    """
    if start > end:
        return Link.empty
    else:
        return Link(start, range_link(start+1, end))

def map_link(f,s):
    """
    >>> map_link(square,range_link(3,6))
    Link(9, Link(16, Link(25)))
    
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest)) 

def filter_link(f,s):
    """
    >>> filter_link(odd, range_link(3,6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(f(s.first), filtered_rest)
    else:
        return filtered_rest
