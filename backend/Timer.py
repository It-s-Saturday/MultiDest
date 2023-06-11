import time

SUCCESS = "success"
FAILURE = "failure"

class Timer:
    def __init__(self, name):
        self.name = name
        self.start = time.time()
        self.end = None
        self.elapsed = None
        self.status = None

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed = round(self.end - self.start, 2)
        self.status = SUCCESS if exc_type is None else FAILURE