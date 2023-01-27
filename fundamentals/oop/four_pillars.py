#Encapsulation example
class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

#Inheritance example
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name) #super() builtin function for taking parent attributes
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")

#Polymorphism(means takes many forms)
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")

#Abstraction  Abstraction is an extension of Encapsulation, and we can hide attributes or methods that a Barista doesn't need to know about, like a CoffeeM
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()



# python code below! swap
arr = [1,3,5,7]
arr[0], arr[1], arr[2], arr[3] = arr[1], arr[0], arr[3], arr[2]

print(arr[2])

