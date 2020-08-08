import multiprocessing
import random

def compute(results):
    results.append(sum([random.randint(1, 100) for i in range(1000000)]))

class MultiProcessingBase:
    @classmethod
    def base_manager(cls):
        with multiprocessing.Manager() as manager:
            results = manager.list()
            workers = [multiprocessing.Process(target=compute, args=(results,)) for x in range(8)]

        for worker in workers:
        	worker.start()

        for worker in workers:
        	worker.join()

        print ("Results of compute is %s" % results)
        

if __name__ == "__main__":
	MultiProcessingBase.base_manager()        		    

