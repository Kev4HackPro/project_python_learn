def kilometre_miles():
    distance = input('Enter distance in (km): ')
    if distance.isnumeric():
        distance1 = int(distance)
        if distance1 > 0:
            converter = distance1 / 0.6214
            return '{} is the distance in miles'.format(converter)
        else:
            return f"You must enter a positive number"
    else:
        return'You must enter an integer'


print(kilometre_miles())
