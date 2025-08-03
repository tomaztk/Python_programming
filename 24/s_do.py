class Dog:
    def __init__(self, name):
        self.name=name
    def bark(self):
        print(f"{self.name} says wooof!")


class Dog2:
    def __init__(self, name, age):
        self.name = name
        self.age = age



dog1 = Dog("Tomaz")

dog1.bark()

dog2 = Dog2("Benko", 3)

print(dog2.name)
print(dog2.age)