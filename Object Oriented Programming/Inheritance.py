'''
PYTHON OBJECT INHERITANCE

Inheritance is the process by which one class takes the methods and attributes
of another. Newly formed classes are called child classes, and classes that child
class inherit from is called the parent classes.

It is important to note that child classes can override or extend the functionality
of parent classes. In other words, child classes can inherit all of the parent's
attributes and behaviours but can also specify a different behaviour to follow.

When you define a python class, it automatically inherit from the class 'object'
object is the most basic class which is inherited by all other classes in general.
'''

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))
