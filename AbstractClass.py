from abc import ABC,abstractmethod

class trasactionProcessor(ABC):

    @abstractmethod
    def processTransaction(self,method):
        pass


class UPI(trasactionProcessor):

    def processTransaction(self):
        print("You paid using UPI process")

IOB = UPI()
