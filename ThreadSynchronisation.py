"""
Thread synchronisation
"""

import threading

class BookingService(threading.Thread):

    # so lock remains static to the class and would be same for all the threads
    lock = None

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

        if BookingService.lock == None:
            BookingService.lock = threading.Lock()

    def book(self):

        with BookingService.lock:
            print("BOOKED! for",self.name)


b1 = BookingService("b1")
b2 = BookingService("b2")

# start the thread
b1.start()
b2.start()

b1.book()
b2.book()

# wait will the thread execution completes!
b1.join()
b2.join()
