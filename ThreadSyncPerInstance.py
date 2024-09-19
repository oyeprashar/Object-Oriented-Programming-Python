import threading

class BookingService(threading.Thread):


    def __init__(self, name):

        # this makes each object run as a thread
        threading.Thread.__init__(self)
        self.name = name
        self.bookingLock = threading.Lock() # unique lock for each instance

  
    # run function is needed to start the thread
    def run(self):
        
        print(f"Thread {self.name} starting...")
        self.book()

    def book(self):

        # this line makes sure we acquire and release the lock
        with self.bookingLock:
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
