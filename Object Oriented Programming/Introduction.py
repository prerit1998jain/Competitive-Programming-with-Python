'''
Defining a class in python3
'''
# pass here is used as a place holder where code will eventually go.
class Animal:
    pass

'''
All classes create objects, and all objects have certain attributes. You can define
initial attributes, providing them with default values. This method must contain,
atleast one argument as well as self variable, which refers to the object itself.
'''

class Animal:

    # Initializer / Instance attributes
    def __init__(self, name, type):
        self.name = name
        self.type = type


'''
The self variable used above is also an instance of the class. since instances of
a class have varying values of these attributes hence we don't use Animal.name = name
rather used self.name = name.

You will never have to call the __init__() method, it gets called automatically
when you create a new animal instance.
'''

'''
Class Attributes are the attributes which is common to every instance of the class.
'''
class Animal:

    # class attributes
    kingdom = 'animal kingdom'

    # instance attributes
    def __init__(self, name, type):
        self.name = name
        self.type = type

'''
INSTANTIATING OBJECTS:

Instantiating is a fancy word for creating new, unique instance of a class.
'''
# Instantiating two different instances
cat = Animal('kitty', 'CAT')
dog = Animal('tommy', 'DOG')
cat == dog

## Accessing the instance Attributes.
print('{} is a {} and {} is a {}'.format(cat.name,cat.type,dog.name,dog.type))

'''
INSTANCE METHODS

Instance methods are defined inside a class and are used to get the contents of
an instance. They can also be used to perform operations with the attributes of
our objects. Like the __init__ method, the first argument should always be self.
'''

class Animal:

    # Class attributes
    kingdom = "Animal Kingdom"

    # Instance attributes
    def __init__(self, name, type):
        self. name = name
        self.type = type

    # Instance method
    def description(self):
        return("{} is a {}.".format(self.name,self.type))

    def speak(self, sound):
        return "{} says {}.".format(self.name, sound)

# INSTANTIATING
Dog = Animal('Tommy', 'Dog')

# Calling the instance METHODS
print(Dog.description())
print(Dog.speak("Bhow Bhow"))


'''
You can also use the instance methods to update the values of instance Attributes
on the basis of certain behaviours. 
'''
