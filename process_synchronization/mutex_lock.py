import time
import threading

class Mutex:
    def __init__(self):
        self.lock = threading.Lock()

    def acquire(self):
        self.lock.acquire()

    def release(self):
        self.lock.release()

# Test for Mutex Lock
def mutex_test(mutex, process_id):
    print(f"Process {process_id} waiting for mutex lock")
    mutex.acquire()
    print(f"Process {process_id} acquired mutex lock")
    time.sleep(1)  # Simulate process operation in critical section
    print(f"Process {process_id} releasing mutex lock")
    mutex.release()

# Create a Mutex
mutex = Mutex()
threads = [threading.Thread(target=mutex_test, args=(mutex, i)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
