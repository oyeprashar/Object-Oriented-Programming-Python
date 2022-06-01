"""
Making a class singleton in Python
"""

class TransactionProcess:

    __instance = None

    # This method is used to get an instance of the class
    @staticmethod
    def getInstance(transType):
        
        # if the instance does not exists then it creates object and set instance variable to it
        if TransactionProcess.__instance == None:
            TransactionProcess.__instance = TransactionProcess(transType)

        return TransactionProcess.__instance


    def __init__(self,transType):
        
        # restricting creating of more than one object of this class
        if TransactionProcess.__instance != None:
            raise Exception("Object already exists! Use getInstance method!")

        self.transType = transType
        TransactionProcess.__instance = self

UPI = TransactionProcess("UPI")
obj = TransactionProcess.getInstance("UPI")

print(obj.transType)
