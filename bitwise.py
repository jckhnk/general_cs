def bitwise_and(a, b):
    """
    Performs the bitwise 'AND' operation on two integers, and prints out the
    binary representation of the input and output for educational purposes.
    """
    a, b = bin(a)[2:], bin(b)[2:]
    diff = len(a)-len(b)
    if diff > 0:
        b = '0' * diff + b
    elif diff < 0:
        a = '0' * abs(diff) + a
    s = ''
    for i in range(len(a)):
        s += str(int(a[i]) & int(b[i]))
    print "{}\n{}\n{}\n{}".format(a, b, '-'*len(a), s)
    c = sum(map(lambda x: 2**x[0] if int(x[1]) else 0, enumerate(reversed(s))))
    return c

def bitwise_or(a, b):
    """
    Performs the bitwise 'OR' operation on two integers, and prints out the
    binary representation of the input and output for educational purposes.
    """
    a, b = bin(a)[2:], bin(b)[2:]
    diff = len(a)-len(b)
    if diff > 0:
        b = '0' * diff + b
    elif diff < 0:
        a = '0' * abs(diff) + a
    s = ''
    for i in range(len(a)):
        s += str(int(a[i]) | int(b[i]))
    print "{}\n{}\n{}\n{}".format(a, b, '-'*len(a), s)
    c = sum(map(lambda x: 2**x[0] if int(x[1]) else 0, enumerate(reversed(s))))
    return c
    
def bitwise_xor(a, b):
    """
    Performs the bitwise 'XOR' operation on two integers, and prints out the
    binary representation of the input and output for educational purposes.
    """
    a, b = bin(a)[2:], bin(b)[2:]
    diff = len(a)-len(b)
    if diff > 0:
        b = '0' * diff + b
    elif diff < 0:
        a = '0' * abs(diff) + a
    s = ''
    for i in range(len(a)):
        s += str(int(a[i]) ^ int(b[i]))
    print "{}\n{}\n{}\n{}".format(a, b, '-'*len(a), s)
    c = sum(map(lambda x: 2**x[0] if int(x[1]) else 0, enumerate(reversed(s))))
    return c

def bitwise_not(a):
    """
    Performs the bitwise negation of an integer, and prints out the
    binary representation of the input and output for educational purposes.
    """
    a = bin(a)[2:]
    s = ''
    for i in range(len(a)):
        s += str(~int(a[i]))
    s = ''.join(['1' if i == '0' else '0' for i in a])
    print "{}\n{}\n{}".format(a, '-'*len(a), s)
    c = sum(map(lambda x: 2**x[0] if int(x[1]) else 0, enumerate(reversed(s))))
    return c

# In [217]: bitwise_or(123, 156)
# 01111011
# 10011100
# --------
# 11111111
# Out[217]: 255

# In [218]: bitwise_and(123, 156)
# 01111011
# 10011100
# --------
# 00011000
# Out[218]: 24

# In [179]: bitwise_xor(123, 156)
# 01111011
# 10011100
# --------
# 11100111
# Out[179]: 231

# In [215]: bitwise_not(123)
# 1111011
# -------
# 0000100
# Out[215]: 4