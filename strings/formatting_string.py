string_format = 'Hello {}!'
print(string_format.format('Kavita'))
name = 'Sunaina'
age = 22
print('{} is {}'.format(name, age))
# Specifying using index for substitution
end_sem_results = 'Hello {1} {0} your term gpa is {2}'
print(end_sem_results.format('Kelvin', 'Kavita', 3.57))
# Specifying using names for substitution
detail = "{actuary} from {organization} is the patron of {body}"
print(detail.format(actuary='Moses Mutuli,FIA',
                    organization='Sanlam Emerging Markets',
                    body='Actuarial Students Society of Kenya'))

song_of_year = '{artist} sang {song} in {year}'
print(song_of_year.format(year=2020, artist='The Weeknd',
                          song='Blinding Lights'))
print('|{:25}|'.format('25 characters width'))
print('|{:<25}|'.format('left aligned'))  # The default
print('|{:>25}|'.format('right aligned'))
print('|{:^25}|'.format('centered'))
print('{:,}'.format(1243456789))
print('{:<25}'.format('Kavita'))
print('{:>30}'.format('Mwendwa'))
print('{:^25}'.format('Kelvin'))