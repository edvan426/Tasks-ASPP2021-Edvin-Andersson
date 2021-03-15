"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Adds two numbers together.
    
    Parameters
    ----------
    a : int or float
        The number to be added to.
    
    b : int or float
        The number which is added.
    
    Returns
    -------
    a+b : int or float
        The result of addition of a and b.
    
    Examples
    --------
    >>> simple_math.simple_add(2,9)
    11
    >>> simple_math.simple_add(5.3,-7.81)
    -2.51
    """
    return a+b

def simple_sub(a,b):
    """
    Subtracts a number from another.
    
    Parameters
    ----------
    a : int or float
        The number to be subtracted from.
    
    b : int or float
        The number which is subtracted.
    
    Returns
    -------
    a-b : int or float
        The result of subraction of b from a.
    
    Examples
    --------
    >>> simple_math.simple_sub(2,9)
    -7
    >>> simple_math.simple_sub(5.3,-7.81)
    13.11
    """
    return a-b

def simple_mult(a,b):
    """
    Multiplies two numbers.
    
    Parameters
    ----------
    a : int or float
        The number to be multiplied.
    
    b : int or float
        The number which is multiplied by.
    
    Returns
    -------
    a*b : int or float
        The result of multiplying a by b.
    
    Examples
    --------
    >>> simple_math.simple_mult(2,9)
    18
    >>> simple_math.simple_mult(5.3,-7.81)
    -41.392999999999994
    """
    return a*b

def simple_div(a,b):
    """
    Divides a number by another.
    
    Parameters
    ----------
    a : int or float
        The number to be divided.
    
    b : int or float
        The number which is divided by.
    
    Returns
    -------
    a/b : int or float
        The result of dividing a by b.
    
    Examples
    --------
    >>> simple_math.simple_div(16,4)
    4
    >>> simple_math.simple_div(5.3,-7.81)
    -0.678617157490397
    """
    return a/b

def poly_first(x, a0, a1):
    """
    Calculates a first degree polynomial at x.
    
    Parameters
    ----------
    x : int or float
        The indeterminate.
    
    a0 : int or float
        The zeroth degree constant.
    
    a1 : int or float
        The first degree constant.
    
    Returns
    -------
    a0 + a1*x : int or float
        The value of the first degree polynomial at point x.
    
    Examples
    --------
    >>> simple_math.poly_first(1,2,3)
    5
    >>> simple_math.poly_first(-4.37,2.612,-99.2)
    436.11600000000004
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Calculates a second degree polynomial at x.
    
    Parameters
    ----------
    x : int or float
        The indeterminate.
    
    a0 : int or float
        The zeroth degree constant.
    
    a1 : int or float
        The first degree constant.
    
    a2 : int or float
        The second degree constant
    
    Returns
    -------
    a0 + a1*x + a2*(x**2) : int or float
        The value of the first degree polynomial at point x.
    
    Examples
    --------
    >>> simple_math.poly_second(1,2,3,4)
    9
    >>> simple_math.poly_second(-4.37,2.612,-99.2,13)
    684.3757
    """
    return poly_first(x, a0, a1) + a2*(x**2)
