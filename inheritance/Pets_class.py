class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return f"{self.name}says {sound}" 

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}" 


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def __init__(self, name, age, dog_no):
        super().__init__(name, age)
        self.dog = dog_no

    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

    def __str__(self):
        return f"{self.name} who is {self.age} is of dog number {self.dog}"

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6, 'AXC569'), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

b = Bulldog('Sia', 6, 'AXCV5677')
print(b)