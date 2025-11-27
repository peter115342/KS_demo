def is_odd(n):
    """
    Determines if a given number is odd.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is odd, False if n is even.

    Examples:
        >>> is_odd(3)
        True
        >>> is_odd(4)
        False
    """
    return n % 2 != 0
