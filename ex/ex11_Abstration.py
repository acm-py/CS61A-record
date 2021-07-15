def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), '分支必须是树'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left,right = fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right), [left,right])

def count_leaves(tree):
    """Count the leaves of tree T"""
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(tree)])
def leaves(tree):
    """Return a list containing the leaf labels of tree
    >>> leaves(fib_tree(5))
    [1,0,1,0,1,1,0,1]
    """
    if is_tree(tree):
        return [label(tree)]
    else:
        # List of leaf label for each branch
        return sum()

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t)+ 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t),bs)