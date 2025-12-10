def safe_divide(a, b):
    """
    Return a / b as a float.
    If b is 0, raise ValueError with the message
    "Division by zero is not allowed".
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b