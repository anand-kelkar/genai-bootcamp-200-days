def divide(a: float, b: float) -> float:
    """
    Returns the result of dividing a by b.
    Raises an exception if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b