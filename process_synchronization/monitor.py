import time
import threading

class MonitorBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity
        self.condition = threading.Condition()

    def produce(self, item):
        with self.condition:
            while len(self.buffer) == self.capacity:
                self.condition.wait()
            self.buffer.append(item)
            print(f"Produced: {item}")
            self.condition.notify_all()

    def consume(self):
        with self.condition:
            while not self.buffer:
                self.condition.wait()
            item = self.buffer.pop(0)
            print(f"Consumed: {item}")
            self.condition.notify_all()
            return item

# Test for Monitor Buffer
def producer(monitor, items):
    for item in items:
        monitor.produce(item)
        time.sleep(0.5)


def consumer(monitor, count):
    for _ in range(count):
        monitor.consume()
        time.sleep(1)

buffer_capacity = 3
monitor_buffer = MonitorBuffer(buffer_capacity)
items_to_produce = [1, 2, 3, 4, 5]



producer_thread = threading.Thread(target=producer, args=(monitor_buffer, items_to_produce))
consumer_thread = threading.Thread(target=consumer, args=(monitor_buffer, len(items_to_produce)))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
