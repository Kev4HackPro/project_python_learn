# Creating Dictionaries

capital_cities = {'Kenya': 'Nairobi',
                  'South Africa': 'Pretoria',
                  'Seychelles': 'Victoria',
                  'United Kingdom': 'London'}
print(capital_cities)
# The dict() constructor
dict1 = dict(UK='London', Kenya='Nairobi', France='Paris', Germany='Berlin')
dict2 = dict([('USA', 'Washington DC'), ('Spain', 'Madrid')])
# noinspection PyTypeChecker
dict3 = dict((['Russia', 'Moscow'], ['China', 'Beijing']))
print(dict1)
print(dict2)
print(dict3)
# Accessing dictionary items via keys
print('Kenya\'s capital:', capital_cities['Kenya'])
print('Britain\'s capital:', capital_cities.get('United Kingdom'))
# Adding a new entry into a dictionary
capital_cities['Sweden'] = 'Stockholm'
print(capital_cities)
# changing key values
capital_cities['South Africa'] = 'Johannesburg'
print(capital_cities)
# removing items from a dictionary(can be removed using .pop(), .popitem(), del
capital_cities.popitem()  # removes last item in our dictionary
print(capital_cities)
capital_cities.pop('Seychelles')  # deletes key specified
print(capital_cities)
del capital_cities['United Kingdom']   # deletes key specified
print(capital_cities)
capital_cities.clear()  # empties the dictionary
print(capital_cities)
# Iterating over keys
music = {'Martin Garrix': 'High On Life',
         'Avicii': 'Heaven',
         'Chris Kaiga': 'Niko On',
         'Khaligraph Jones': 'Hao'}
for musicia in music:
    print(musicia, end=', ')
    print(music[musicia])
# Values keys and items
for musicia in music.values():
    print('song title:', musicia)

for musicia in music.keys():
    print('Artist Name:', musicia)

for artist, song in music.items():
    print(artist, ':', song)


# checking key membership
print('Martin Garrix' in music)
print('Dar es Salaam' not in capital_cities)
# obtaining length of a dictionary
print(len(music))
# Nesting dictionaries
seasons = {'Spring': ('Apr', 'May', 'Jun'),
           'Winter': ('November', 'December', 'January'),
           'Summer': ('February', 'March'),
           'Autumn': ('July', 'August', 'September')}
print(seasons['Spring'])
print(seasons['Winter'][::-1])

for changes in seasons:
    print(changes, end=': ')
    print(seasons[changes])

family = {'Child1':
              {'name': 'Marion',
               'age': 15,
               'gender': 'female'},
          'Child2': {'name': 'Omondi',
                     'age': 17,
                     'gender': 'male'},
          'Child3': {'name': 'Kelvin',
                     'age': 19,
                     'gender': 'male'}}
for members in family:
    print(members, end=': ')
    print(family[members])

for values in family.values():
    print(values)

print(family['Child1']['name'])