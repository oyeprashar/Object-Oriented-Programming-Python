"""
- The problem with multi-threading with classes is that they needs a run function to be overwritten and that takes no arguments, so to make a multi-threaded function with args, we need
to declare it outside and then call `threading.Thread(target = func_name, args = (arg1, arg2))`

- thread start and thread join is needed to start the thread and wait for its execution
"""

import threading

 
class Bank:
    
    def __init__(self, accountHolderName):
        self.accountHolderName = accountHolderName

def transaction(bankObject, amount):
    print("beep boop beep.....")
    print("-- Debited :", amount," --")
    print("Thank you : ", bankObject.accountHolderName)


account = Bank("Shubham Prashar")
thread = threading.Thread(target = transaction, args = (account, 9000))

thread.start()
thread.join()


# account.run("9000")
