import threading

class TestClass:

    lock = threading.Lock()

    def printName(self, name):
        for _ in range(1):
            lock.acquire()
            print(name)
            lock.release()

testObject = TestClass()
testObject.printName("Shubham")
