class Dog:
    """modelling a dog"""

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} sat!")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie',6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

my_dog2 = Dog('Dog',6)

print(f"My dog's name is {my_dog2.name}.")
print(f"My dog is {my_dog2.age} years old.")
my_dog2.sit()
my_dog2.roll_over()