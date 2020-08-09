# same computation with threading this time
import random
import threading

results = []

def compute():
    results.append(sum([random.randint(1, 100) for i in range(1000000)]))

class ThreadingWorkers:
	@classmethod
	def workers(cls):
		workers_list = [threading.Thread(target=compute) for x in range(8)]
		for worker in workers_list:
			worker.start()
		for worker in workers:
			worker.join()
		print("Computed thread results: %s" % results)


if __name__ == "__main__":
	thread_based_workers = ThreadingWorkers.workers()		
