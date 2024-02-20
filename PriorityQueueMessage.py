import queue
import threading

class PriorityMessageQueue:
    """
    Priority Message Queue implementation using Python's PriorityQueue.
    """

    def __init__(self):
        """
        Initialize PriorityMessageQueue with a thread-safe PriorityQueue.
        """
        self.queue = queue.PriorityQueue()
        self.lock = threading.Lock()

    def enqueue(self, message, priority):
        """
        Enqueue a message with a specified priority.
        """
        with self.lock:
            self.queue.put((priority, message))

    def dequeue(self):
        """
        Dequeue and return the highest priority message from the queue.
        """
        with self.lock:
            if not self.queue.empty():
                return self.queue.get()[1]
            else:
                return None

    def peek(self):
        """
        Peek and return the highest priority message without removing it from the queue.
        """
        with self.lock:
            if not self.queue.empty():
                return self.queue.queue[0][1]
            else:
                return None

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        with self.lock:
            return self.queue.empty()
