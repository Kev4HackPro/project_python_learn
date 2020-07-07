from math import sin, cos, acos

a = float(input('Latitude, first point: '))
b = float(input('Longitude, first point: '))
a1 = float(input('Latitude, second point: '))
b1 = float(input('Longitude, second point: '))
bearing = [(a, b), (a1, b1)]
distance = 6731.01 * acos(sin(a)) * sin(a1) + cos(a) * cos(a1) * cos(b - b1)
print('Distance is:' + " " + str(distance))
