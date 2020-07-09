class DivideByYWhenZeroException(Exception):
    """Chaining exceptions"""


def divide(x, y):
    try:
        result = x / y
        return result
    except Exception as e:
        raise DivideByYWhenZeroException from e


def main():
    divide(6, 0)


if __name__ == '__main__':
    main()