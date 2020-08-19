from concurrent import futures
import random

def compute():
    return sum([random.randint(1, 100) for i in range(1000000)])


class FutureThreadPool:
    def __init__(self, workers):
        self.workers = workers
    
    def future_threadpool(self):
        with futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = [executor.submit(compute) for _ in range(8)]

        results = [f.result() for f in futures]
        print ("Compute result is: %s" % (results)


if __name__ == "__main__":
    future_thread = FutureThreadPool(8)





