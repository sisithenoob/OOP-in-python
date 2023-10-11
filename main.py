class Item:
    pay_rate = 0.8# the pay rate after 20% discount
    all = []#list of all item in our shop

    def __init__(self, name: str, price: float, quantity = 0):
        #Run validation to the received arguments
        assert price >= 0, f" Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)#append the instance of the class to the list of all the item in our shop

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Computer", 1000, 2)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

for instance in Item.all:
    print(instance.name)

print(Item.all)