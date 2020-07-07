age = int(input('Enter your age: '))
status = None
if (age > 12) and age < 20:
    status = 'teenager'
    print(f"You are a {status}")
else:
    status = 'not a teenager'
    print(f"You are {status}")

# Or can write your code like this
status1 = ('teenager' if (age > 12) and age < 20 else
           'not teenager')
print(status1)