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
