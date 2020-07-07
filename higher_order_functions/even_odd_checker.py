def odd_even_checker(num):
    if num == 'even':
        return lambda n: n % 2 == 0
    elif num == 'positive':
        return lambda n: n >= 0
    elif num == 'negative':
        return lambda n: n < 0
    else:
        raise(ValueError('Unknown request'))


f1 = odd_even_checker('even')
f2 = odd_even_checker('positive')
f3 = odd_even_checker('negative')

print(f1(3))
print(f2(9))
print(f3(-7))
