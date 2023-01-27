#Create a Pet class with the pet attributes listed above.
# implement __init__( name , type , tricks ):

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 30
        self.noise= "Bark"
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Eat Eat Eat {(food)}")
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print("I love walks")
        return self
# noise() - prints out the pet's sound
    def call_noise(self):
        print(f"{self.noise}")
        return self
#Create a Ninja class with the ninja attributes listed above.
class Ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Goku
        self.treats = treats
        self.pet_food = pet_food
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self,):
        self.pet.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.call_noise()
        return self
    def display_pet_info(self):
        print("------------")
        print(f"Name-{self.pet.name}")
        print(f"Health-{self.pet.health}")
        print(f"Energy- {self.pet.energy}")
        print("------------")
treats = ["Bacon", "Pork", "Turkey"]
food = ["Biscuits", "Chicken"]

Goku = Pet("Goku", "Pitbull", "Catch")
Ginyu = Ninja("Captain", "Ginyu", Goku, treats, food)


# Ginyu.feed().walk().bathe().display_pet_info()

