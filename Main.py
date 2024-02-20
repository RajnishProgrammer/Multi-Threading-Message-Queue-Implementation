import time
from PriorityQueueMessage import PriorityMessageQueue
from ThreadPool import ThreadPool
import threading

def send_message(sender, receiver, message, priority):
    """
    Send a message from sender to receiver with a specified priority.
    """
    receiver.receive_message(message, priority)

def action(message, name):
    """
    Define action to be performed upon receiving a message.
    """
    print(f"Received message from {name}: {message}")
    # Simulate processing time
    time.sleep(1)

class ReceiverThread(threading.Thread):
    """
    Receiver Thread class to receive and process messages.
    """

    def __init__(self, name, queue, thread_pool):
        super().__init__()
        self.name = name
        self.queue = queue
        self.thread_pool = thread_pool

    def run(self):
        """
        Run method of ReceiverThread to receive and process messages.
        """
        while not self.queue.is_empty():
            message = self.queue.dequeue()
            if message:
                self.thread_pool.submit_task(lambda: action(message, self.name))
            else:
                pass

    def receive_message(self, message, priority):
        """
        Receive and enqueue a message with a specified priority.
        """
        self.queue.enqueue(message, priority)

if __name__ == "__main__":
    # Initialize PriorityMessageQueue and ThreadPool
    queue1 = PriorityMessageQueue()
    queue2 = PriorityMessageQueue()
    thread_pool = ThreadPool(num_threads=5)

    # Create ReceiverThread instances
    receiver1 = ReceiverThread('Receiver1', queue1, thread_pool)
    receiver2 = ReceiverThread('Receiver2', queue2, thread_pool)

    # Send messages between ReceiverThread instances
    send_message(sender=receiver1, receiver=receiver2, message='Hello', priority=1)
    send_message(sender=receiver1, receiver=receiver2, message='World', priority=2)
    send_message(sender=receiver1, receiver=receiver2, message='Planet', priority=3)
    send_message(sender=receiver2, receiver=receiver1, message='Hi', priority=1)
    send_message(sender=receiver2, receiver=receiver1, message='Galaxy', priority=2)
    send_message(sender=receiver2, receiver=receiver1, message='Star', priority=3)

    # Start ReceiverThread instances
    receiver1.start()
    receiver2.start()

    # Wait for ReceiverThread instances to finish
    receiver1.join()
    receiver2.join()
