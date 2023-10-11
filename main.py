import csv

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

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as items_csv:#open the csv file to read it only into a variable call items_csv
            items_reader = csv.DictReader(items_csv)#set all the the item as dict in items_reader
            items = list(items_reader)#set all the ditionaries of our item into a list of dictionaries
        #iterate through each dictionaries of our list of items
        for item in items:
            Item( name = item.get("name"), #Instantiate new instances of class Items with the value of our dict.
                  price = float(item.get("price")),
                  quantity = int(item.get("quantity"))
                )

    @staticmethod
    def is_integer(num):
        #we will count out the decimal that are point zero per example : 100.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

print(Item.is_integer(7.5))
