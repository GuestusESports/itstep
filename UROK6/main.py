class Human:
    def __init__(self, name="Human"):
        self.name=name

class Auto:
    def __init__(self,brand):
        self.brand=brand
        self.passangers=[]
def add_passenger(self, human):
    self.passengers.append(human)

def print_passengers_names(self):
    if self.passengers!=[]:
        print(f"Names of {self.brand} passengers:")
        for passenger in self.passengers:
            print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")
nick=Human("Nick")
arkady=Human("Arkady")
car=Auto("Жигуль")
car.add_passenger(nick)
car.add_passenger(arkady)
car.print_passengers_names()