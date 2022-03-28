from abc import ABC, abstractmethod

class Vehicle(ABC):

    @property
    @abstractmethod
    def color(self):
        pass
    
class Car(Vehicle):

    def __init__(self,_color):
        self._color = _color
    
    # this will go and get color fron @property color function
    def getColor(self):
        return self.color

    @property
    def color(self):
        return self._color
    
car = Car("RED")
print(car.color)
