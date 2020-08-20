import futurist
from futurist import waiters
import random

def compute():
    return sum([random.randint(1,100) for i in range(10000)])

class FuturistThreadPool:
    def __init__(self, worker):
        self.worker = worker
    def thread_pool_executor(self):
        with futurist.ThreadPoolExecutor(max_workers=self.worker) as executor:
            futures = [executor.submit(compute) for _ in range(8)]
            print(executor.statistics)

        results = waiters.wait_for_all(futures)
        print (executor.statistics)
        print ("Results is %s" % [r.result() for r in results.done])


