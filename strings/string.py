# Representing strings
single_coma = 'How was your day?'
double_comma = "Tracy's character is wanting"
triple_comma = """Nairobi is the capital city of the African nation, Kenya"""
print(single_coma)
print(double_comma)
print(triple_comma)

# String concatenation
first_name = 'Kelvin'
last_name = ' Kavita'
full_name = first_name + last_name
print(full_name)

# Accessing string characters
favourite_team = 'Manchester United'
print(favourite_team[4])

# Accessing subset of strings
print(favourite_team[0:])
print(favourite_team[1:-1])
print(favourite_team[-1])
print(favourite_team[-2])
print(favourite_team[1:5])

title = 'The good, the bad, and the ugly.'
# splitting where there is space
print(title.split(' '))
# splitting where there is a comma
print(title.split(','))
# splitting where there is a fullstop
print(title.split('.'))
print(type(title))
# length of a string
print(len(title))
# counting strings
my_string = 'Count, the number of spaces'
print("my_string.count(' '): ", my_string.count(' '))
title = "Count, the, number, of, commas, in, the, text"
print("Commas in title:", title.count(','))
profession = 'Actuary'
print(profession.count('t'))
# Replacing strings
goal = 'To build a financial technology to revolutionize the Kenyan tech space '
print(goal.replace('Kenyan', 'African'))
# Finding substrings
print(goal.find('To'))
print('Kelvin Kavita'.find('Kavita'))
# Converting other types to strings
msg = 'Hello Kavita you are approaching ' + str(21)
print(msg)
# comparing strings
print('Kavita' == 'kavita')
print('Mwendwa' == 'Kelvin')
print('Sunaina' == 'Sunaina')
print('Sunaina' != 'Sharon')
# Other string methods

some_string = 'Hello World'
print('Testing a String')
print('-' * 20)
print('some_string', some_string)
print("some_string.startswith('H')",
      some_string.startswith('H'))
print("some_string.startswith('h')",
      some_string.startswith('h'))
print("some_string.endswith('d')", some_string.endswith('d'))
print('some_string.istitle()', some_string.istitle())
print('some_string.isupper()', some_string.isupper())
print('some_string.islower()', some_string.islower())
print('some_string.isalpha()', some_string.isalpha())
print('String conversions')
print('-' * 20)
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase())
print('String leading, trailing spaces', " xyz ".strip())
