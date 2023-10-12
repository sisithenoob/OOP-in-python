import csv

class Item:
    pay_rate = 0.8# the pay rate after 20% discount
    all = []#list of all item in our shop

    def __init__(self, name: str, price: float, quantity = 0):
        #Run validation to the received arguments
        assert price >= 0, f" Price {price} is not equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not equal or greater than zero"

        #assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)#append the instance of the class to the list of all the item in our shop

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception("Your name is too long we only accept 10 character")
        else:
            self.__name = new_name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise Exception("We cannot sell something that is worth nothing")
        else:
            self.__price = new_price

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
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"
    