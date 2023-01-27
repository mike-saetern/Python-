class Store:
    def __init__(self,name,products):
        self.name = name
        self.products = products

    def add_product(self,new_product):
        self.new_product = new_product
        self.products.append(new_product)
        return self

    def sell_product(self,products):
        self.products = products
        self.products.remove() #code does not work
        return self

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self,percent_change,is_increased):
        if is_increased is True:
            self.price += percent_change
        else:
            self.price -= percent_change
        return self

    def print_info(self):
        print("-----------------------")
        print(f"Product - {self.name}")
        print(f"Category - {self.category}")
        print(f"Price - ${self.price}")
        print("-----------------------")
        return self

lowes = Store("Lowes", ["Tools", "Tile", "Wood"])
dirt = Product("dirt", 75, "yard")
sink = Product("sink", 200, "bathroom")

lowes.add_product("Knife")
print(lowes.products)

lowes.sell_product("Tools")