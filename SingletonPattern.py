from abc import ABC,abstractmethod

class trasactionProcessor(ABC):

    @abstractmethod
    def processTransaction(self,method):
        pass


class UPI(trasactionProcessor):

    __instance = None

    @staticmethod
    def getInstance():

        if UPI.__instance == None:
            UPI.__instance = UPI()

        return UPI.__instance

    def __init__(self):

        if UPI.__instance != None:
            raise Exception("Object already exits! Use getInstance instead!")

        UPI.__instance = self


    def processTransaction(self):
        print("You paid using UPI process")


IOB = UPI()
print(IOB)

IOBVasundhara = UPI.getInstance()

print(IOBVasundhara)

