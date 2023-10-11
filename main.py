class Item:
    def __init__(self):
        print("I am created !!!!")

    def calculate_total_price(self, price, quantity):
        return self.price * self.quantity

item1 = Item()
item1.name = "phone"
item1.price = 100
item1.quantity = 5
total_price_item1 =  item1.calculate_total_price(item1.price, item1.quantity)
print(total_price_item1)

item2 = Item()
item2.name = "computer"
item2.price = 2500
item2.quantity = 2
total_price_item2 = item2.calculate_total_price(item2.price, item2.quantity)
print(total_price_item2)