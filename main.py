class Item:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)

item2 = Item("Computer", 2500, 2)
item2.has_numpad = False

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price())