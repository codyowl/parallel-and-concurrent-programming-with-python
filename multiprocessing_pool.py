import multiprocessing
import random

def compute(n):
	return sum([random.randint(1, 100) for i in range(1000000)])

class MultiProcessPool:
	def star_workers(self, number_of_workers):
		self.number_of_workers = number_of_workers

	def start_pool(self):
		pool = multiprocessing.Pool(processes=self.number_of_workers)
		print("Compute results %s" % pool.map(compute, range(8)))


if __name__ == "__main__":
	multiprocessing_pool = MultiProcessPool()
	multiprocessing_pool.star_workers(10)
	multiprocessing_pool.start_pool()