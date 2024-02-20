from concurrent.futures import ThreadPoolExecutor

class ThreadPool:
    """
    Thread Pool implementation using Python's ThreadPoolExecutor.
    """

    def __init__(self, num_threads):
        """
        Initialize ThreadPool with a ThreadPoolExecutor.
        """
        self.executor = ThreadPoolExecutor(max_workers=num_threads)

    def submit_task(self, task):
        """
        Submit a task to the thread pool for execution.
        """
        return self.executor.submit(task)
