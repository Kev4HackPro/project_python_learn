import string

template = string.Template('$artist sang $song in $year')
print(template.substitute(artist='Martin Garrix', song='Scared to be lonely', year=2017))
actuary_future = string.Template('$name has revolutionized the $industry in $country')
print(actuary_future.substitute(name='Kelvin Kavita, FeAsk,ERM.', industry='Financial industry', country='Kenya'))
song = string.Template("$artist sang $song in $year")
print(song.substitute(artist='Ed Sheeran', song='Shape of you', year=2017))
d = dict(artist='Sauti Sol', song='Melanin',
         year=2017)
print(template.substitute(d))
risk = string.Template('$name has worked in the $industry industry for $years')
d = dict(name='Kelvin Kavita, FeAsk, CERA', industry='Enterprise Risk Management')
print(risk.safe_substitute(d))
