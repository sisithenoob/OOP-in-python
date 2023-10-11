class Item:
    pay_rate = 0.8# the pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity = 0):
        #Run validation to the received arguments
        assert price >= 0, f" Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        pass

item1 = Item("Phone", 100, 5)
item2 = Item("Computer", 2500, 2)

print(Item.__dict__) #all attribute of the class level  
print(item1.__dict__) # all attribute of the instance level