"""
- This code is about how we can have the same lock for all the objects of a single class.
- Can be useful in scenarios like writing to DB and we want a single object to write at a time 
"""
import threading

class BookingService(threading.Thread):

    # a static variable to lock the execution of book function
    bookingLock = None

    def __init__(self, name):

        # this makes each object run as a thread
        threading.Thread.__init__(self)
        self.name = name

        # if lock is None, initialise it
        if BookingService.bookingLock is None:
            BookingService.bookingLock = threading.Lock()

    # run function is needed to start the thread
    def run(self):
        
        print(f"Thread {self.name} starting...")
        self.book()

    def book(self):

        # this line makes sure we acquire and release the lock
        with BookingService.bookingLock:
            print(f"Thread {self.name} is booking...")
            print(f"BOOKED! for {self.name}")
        print(f"Thread {self.name} finished booking.")


# Create two threads
b1 = BookingService("b1")
b2 = BookingService("b2")

# Start the threads
b1.start()
b2.start()

# Wait for both threads to complete
b1.join()
b2.join()
