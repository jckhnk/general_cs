def has_substr(string, substr):
    """
    Checks a given string for the presence of a given substring.
    """
    if string == substr:
        return True
    n = len(substr)
    for i in range(len(string)):
        if string[i:i+n] == substr:
            return True
    return False

# In [228]: has_substr('hello world', 'hello')
# Out[228]: True

# In [229]: has_substr('hello world', 'ell')
# Out[229]: True

# In [230]: has_substr('hello world', 'ellw')
# Out[230]: False