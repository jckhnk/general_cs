def atoi1(a):
    """
    Converts an ASCII string to an integer, like atoi() in C.

    %timeit atoi1('-123456789')
    100000 loops, best of 3: 8.25 µs per loop
    """
    neg = False
    if a[0] == '-':
        neg = True
        a = a[1:]
    i = 0
    n = len(a)
    for k in range(n):
        i += int(a[k])
        if k < n - 1:
            i *= 10
    if neg:
        return -i
    else:
        return i

def atoi2(a):
    """
    Converts an ASCII string to an integer, like atoi() in C.

    Slightly faster because it trades an if statement and a len()
    for single integer multiplication and division operations:

    %timeit atoi2('-123456789')
    100000 loops, best of 3: 7.43 µs per loop
    """
    neg = False
    if a[0] == '-':
        neg = True
        a = a[1:]
    i = 0
    for digit in a:
        i += int(digit)
        i *= 10
    if neg:
        return -i/10
    else:
        return i/10

# In [238]: atoi1('1234567890')
# Out[238]: 1234567890

# In [239]: atoi1('-1234567890')
# Out[239]: -1234567890

# In [240]: atoi2('1234567890')
# Out[240]: 1234567890

# In [241]: atoi2('-1234567890')
# Out[241]: -1234567890