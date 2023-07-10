def clamp(value: int, min_val: int, max_val: int) -> int:
    """
    Clamps the value between the provided minimum and maximum.

    :param value: The value to clamp
    :param min_val: The minimum value to allow
    :param max_val: The maximum value to allow
    :return: Returns the value clamped between the minimum and maximum
    """
    if value <= min_val:
        return min_val
    if value >= max_val:
        return max_val
    return value
