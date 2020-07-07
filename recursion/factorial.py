# Calculating factorial of a number using recursion
def factorial(num):
    """
    termination condition guaranteed to execute when num is 0. This is the base case.
    We cannot reduce the problem down further as 0! is 1.
    The function recursively calls itself but with n-1 as the argument. This means every time
    it calls itself value of n is smaller

    """
    if num == 0:  # terminating condition
        return 1  # base case
    else:
        result = num * factorial(num - 1)  # Recursive part
        return result


print(factorial(5))


# How above function behaves

def factorial_t(num, depth=1):
    """Hii function isikupatie stress, i don't think ata unafaa kujua...yenye iko huko juu ndo important, just
    shows you how the above function works
    """
    if num == 0:
        print('\t' * depth, 'Returning 1')
        return 1
    else:
        print('\t' * depth, 'Recursively calling factorial(', num - 1,
              ')')
        result = num * factorial_t(num - 1, depth + 1)
        print('\t' * depth, 'Returning: ', result)
        return result


print('Calling factorial_t(5)')
print(factorial_t(5))
