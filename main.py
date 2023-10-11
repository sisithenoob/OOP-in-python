class Item:
    def __init__(self, name):
        self.name = name
        print(f"an instance created : {name}")

    def calculate_total_price(self, price, quantity):
        return self.price * self.quantity

item1 = Item("Phone")
item1.price = 100
item1.quantity = 5


item2 = Item("Computer")
item2.price = 2500
item2.quantity = 2

print(item1.name)
print(item2.name)