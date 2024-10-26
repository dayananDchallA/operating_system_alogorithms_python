import time
import threading

class Barrier:
    def __init__(self, count):
        self.count = count
        self.current_count = 0
        self.condition = threading.Condition()

    def wait(self):
        with self.condition:
            self.current_count += 1
            if self.current_count == self.count:
                self.condition.notify_all()  # Release all waiting threads
            else:
                self.condition.wait()

# Test for Barrier
def barrier_test(barrier, process_id):
    print(f"Process {process_id} reached barrier")
    barrier.wait()
    print(f"Process {process_id} passed barrier")

# Create a Barrier for 3 processes
barrier = Barrier(3)
threads = [threading.Thread(target=barrier_test, args=(barrier, i)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
