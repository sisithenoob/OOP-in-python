class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, price, quantity):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)

item2 = Item("Computer", 2500, 2)

print(item1.name)
print(item1.price)
print(item1.quantity)