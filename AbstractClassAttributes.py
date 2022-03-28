from abc import ABC, abstractmethod, abstractproperty

class Vehicle(ABC):

    @abstractproperty
    def color(self):
        pass
    
class Car(Vehicle):

    def __init__(self,color):
        self.color = color
