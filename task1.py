import json
from datetime import date, datetime

count = 1

class Regular():
    def __init__(self):
        with open("C:\\cygwin\\home\\ntele\\py_lab3\\data1.json", "r") as json_file:
            json_object = json.load(json_file)
        global count
        if count > json_object["ammount of tickets"]:
            raise OverflowError(f'More than {json_object["ammount of tickets"]} trying to be created')
        else: 
            self.price = json_object["price"]
            self.id = count
            count += 1
    def get_id(self):
        return self.id

    def get_price(self):
        return self.price
        
    def __str__(self):
        return f'Ticket id: {self.id} Price of ticket: {self.price}'
        
class Student(Regular):
    def __init__(self):
        
        with open("C:\\cygwin\\home\\ntele\\py_lab3\\data1.json", "r") as json_file:
            json_object = json.load(json_file)
        global count
        if count > json_object["ammount of tickets"]:
            raise OverflowError(f'More than {json_object["ammount of tickets"]} trying to be created')
        else: 
            self.price = json_object["price"]//2
            self.id = count
            count += 1


class Advance(Regular):
    def __init__(self):
        with open("C:\\cygwin\\home\\ntele\\py_lab3\\data1.json", "r") as json_file:
            json_object = json.load(json_file)
        global count
        if count > json_object["ammount of tickets"]:
            raise OverflowError(f'More than {json_object["ammount of tickets"]} trying to be created')
        else: 
            self.price = json_object["price"] - (json_object["price"] * 0.4)
            self.id = count
            count += 1
        

class Late(Regular):
    def __init__(self):
        with open("C:\\cygwin\\home\\ntele\\py_lab3\\data1.json", "r") as json_file:
            json_object = json.load(json_file)
        global count
        if count > json_object["ammount of tickets"]:
            raise OverflowError(f'More than {json_object["ammount of tickets"]} trying to be created')
        else: 
            self.price = json_object["price"] + (json_object["price"] * 0.1)
            self.id = count
            count += 1
            
class Event:
    def __init__(self, regular_price, number_of_tickets, event_date):
        self.price = regular_price
        self.number = number_of_tickets
        self.eventdate = event_date
        data = {
            "price":self.price,
            "ammount of tickets":self.number,
            "date":self.eventdate
        }
        with open("C:\\cygwin\\home\\ntele\\py_lab3\\data1.json", "w") as json_file:
            json.dump(data, json_file, indent=2)
        self.ticket = None
        
    @property 
    def price(self):
        return self.__price

    @price.setter
    def price(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError("Price must be a decimal")
        if not data:
            raise TypeError("Field cannot be empty")
        self.__price = data

    @property 
    def eventdate(self):
        return self.__eventdate

    @eventdate.setter
    def eventdate(self, data):
        if not isinstance(data, str):
            raise TypeError("Date must be a string")
        if not data:
            raise TypeError("Field cannot be empty")
        self.__eventdate = data
    
    @property 
    def number(self):
        return self.__number

    @number.setter
    def number(self, data):
        if not isinstance(data, int):
            raise TypeError("Ammount of tickets must be a number")
        if not data:
            raise TypeError("Field cannot be empty")
        self.__number = data

    def days_between(event_date):
 
        currentdate = datetime.today()
        eventdate = datetime.strptime(event_date, "%d.%m.%Y")
        difference = (eventdate - currentdate).days
        return difference

    
    
    def buy_ticket(self):
        with open("C:\\cygwin\\home\\ntele\\py_lab3\\data1.json", "r") as json_file:
            json_object = json.load(json_file)
        days_difference = Event.days_between(json_object["date"])
        type = input("Are you a student? 1 - no, 0 - yes: ")
        if not type:
            self.ticket = Student()
        else:
            if days_difference > 60:
                self.ticket = Advance()
            elif days_difference <10:
                self.ticket = Late()
            else: 
                self.ticket = Regular()
       
        id = str(self.ticket.get_id()) 
        with open("py_lab3\\tickets.json", "r") as file:
            json_base = json.load(file)
        if not id in json_base:
            json_base[id] = {
                "ticket_id": self.ticket.get_id(),
                "ticket_type": self.ticket.__class__.__name__,
                "price": self.ticket.get_price()
            }
            json.dump(json_base, open("C:\\cygwin\\home\\ntele\\py_lab3\\tickets.json", "w"), indent = 2)
    
    def ticket_price_by_id(self, ticket_id):
        with open ("py_lab3\\tickets.json", "r") as file:
            json_base = json.load(file)
        return json_base[str(ticket_id)]["price"]

    def __str__(self):
        return f'Price: {self.price}, Number of tickets: {self.number}'



x = Event(100, 10, "14.12.2021")
x.buy_ticket()
x.buy_ticket()
print(x.ticket_price_by_id(2))










