def kilometre_to_miles():
    unit_in_kilometres = int(input("Distance in (Km) to be converted: "))
    converter = unit_in_kilometres / 0.6214
    return f'Your distance in miles is {converter}'


print(kilometre_to_miles())
