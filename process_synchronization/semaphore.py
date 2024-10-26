import threading
import time

class Semaphore:
    def __init__(self, max_count):
        self.counter = max_count
        self.condition = threading.Condition()

    def acquire(self):
        with self.condition:
            while self.counter == 0:
                self.condition.wait()
            self.counter -= 1

    def release(self):
        with self.condition:
            self.counter += 1
            self.condition.notify()

# Test for Semaphore
def semaphore_test(semaphore, process_id):
    print(f"Process {process_id} waiting to enter critical section")
    semaphore.acquire()
    print(f"Process {process_id} entered critical section")
    time.sleep(1)  # Simulate process operation in critical section
    print(f"Process {process_id} leaving critical section")
    semaphore.release()

# Create a semaphore that allows 2 processes at a time
sem = Semaphore(2)
threads = [threading.Thread(target=semaphore_test, args=(sem, i)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
