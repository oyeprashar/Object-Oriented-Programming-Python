from abc import ABC,abstractmethod

class trasactionProcessor(ABC):

    @abstractmethod
    def processTransaction(self,method):
        pass


# The class implementing the abstract class needs to overwrite all the mothods of the abstract class.
# If we dont implement all the methods of the abstract class then we wont be able to make object so this class as well
class UPI(trasactionProcessor):

    def processTransaction(self):
        print("You paid using UPI process")

IOB = UPI()
