""" Optional Questions for Lab 10 """

from lab10 import *

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while True:
        yield n
        if n == 1:
            break
        elif n % 2 == 0:
            n //= 2
        else:
            n = n*3 + 1

# Q6
def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> repeated([10, 9, 10, 9, 9, 10, 8, 8, 8, 7], 2)
    9
    >>> repeated([10, 9, 10, 9, 9, 10, 8, 8, 8, 7], 3)
    8
    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    i, n, prev = 0, 0, None
    for x in iter(t):
        if i != 0 and x == prev:
            n += 1
        else:
            n = 1
        if n == k:
            return x
        prev = x
        i += 1


# Q7
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. s0 or s1 may be infinite
    sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0, None), next(i1, None)
    "*** YOUR CODE HERE ***"
    while e0 is not None and e1 is not None:
        if e0 == e1:
            yield e0
            e0 = next(i0, None)
            e1 = next(i1, None)
        elif e0 < e1:
            yield e0
            e0 = next(i0, None)
        else:
            yield e1
            e1 = next(i1, None)
    if e0 is None:
        yield e1
        yield from i1
    if e1 is None:
        yield e0
        yield from i0

# Q8
def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def get_remainders_generator(m, i):
        if m >= i and i != 0:
            x = i
        else:
            x = m
        while True:
            yield x
            x += m
    for i in range(m):
        yield get_remainders_generator(m, i)
# Q9
def zip_generator(*iterables):
    """
    Takes in any number of iterables and zips them together.
    Returns a generator that outputs a series of lists, each
    containing the nth items of each iterable.
    >>> z = zip_generator([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    "*** YOUR CODE HERE ***"
    iters = [iter(i) for i in iterables]
    while True:
        lst = []
        for itr in iters:
            x = next(itr, None)
            if x is None:
                return
            lst += [x]
        yield lst
