from abc import ABC, abstractmethod

class Vehicle(ABC):

    @property
    @abstractmethod
    def color(self):
        pass
    
class Car(Vehicle):

    def __init__(self,color):
        self.color = color
