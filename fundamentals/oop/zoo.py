import random

class animal():
    def __init__(self,type,name):
        self.type = type
        self.name = name
        self.health = 100
        self.happiness = 75

    def feed(self):
        self.health += random.randint(1,10)
        self.happiness += random.randint(1,10)
        return self

    def display_info(self):
        print("---------------")
        print(f"Name - {self.name}")
        print(f"Health - {self.health}")
        print(f"Happiness - {self.happiness}")
        print("---------------")
        return self

class zoo(animal):
    def __init__(self,name):
        super().__init__(type, name)
        self.name = name
        self.animals = []

    def add_animal(self,name):
        self.animals.append(name)
        return self

    def display_animals(self):
        print("---------------")
        print(f"Welcome to {self.name}")
        print(f"These are our animals {self.animals}")
        print("---------------")
        return self

conor = animal("lion", "conor")
renea = animal("tiger", "renea")
retreat = zoo("Super Zoo")
retreat.add_animal("lion").add_animal("tiger").display_animals()
conor.feed().display_info()
renea.feed().display_info()


