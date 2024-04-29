def none_to_zero(value):
    """
    Convert the value to 0 if it is None
    or Falsy
    """
    if not value:
        return 0
    return value
