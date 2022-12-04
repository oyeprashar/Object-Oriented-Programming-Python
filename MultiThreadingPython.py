import threading

class TestClass:

    def __init__(self):
        self.lock = threading.Lock()

    def printName(self, name):
        for _ in range(1):
            self.lock.acquire()
            print(name)
            self.lock.release()

testObject = TestClass()
testObject.printName("Shubham")
