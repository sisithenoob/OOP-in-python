from item import Item

Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        #call to super function to have all attributes and methods of the parent class (Item)
        super().__init__(
            name, price, quantity
        )
        
        #Run validation to the received arguments
        assert broken_phones >= 0, f"Broken Phone {broken_phones} is not equal or greater than zero"

        #assign to self object
        self.broken_phones = broken_phones

Phone1 = Phone("Iphone10", 1500, 6)

print(Item.all)
print(Phone.all)