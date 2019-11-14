class Dog:
    def __init__(self, name, specie, age):
        self.name = name
        self.specie = specie
        self.age = age

    def speak(self):
        print("gua gua")

my_dog = Dog("Doggy", "buldog", 12)
my_dog_1 = Dog("taizo", "buldog", 2)
my_dog_2 = Dog("Max", "buldog", 5)
