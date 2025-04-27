class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
        
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()  # Output: Buddy says Woof! 
dog2.bark()  # Output: Max says Woof!
print(f"{dog1.name} is {dog1.get_age()} years old.")  # Output: Buddy is 3 years old.        