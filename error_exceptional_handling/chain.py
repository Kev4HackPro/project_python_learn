class DivideByYWhenZeroException(Exception):
    """Chaining exceptions"""


def divide(x, y):
    try:
        result = x / y
    except Exception as e:
        raise DivideByYWhenZeroException from e


divide(6, 4)
