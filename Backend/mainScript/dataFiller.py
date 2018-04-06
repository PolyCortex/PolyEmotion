import time
import multiprocessing 
from collections import deque
import numpy as np

class fillerWorker(multiprocessing.Process):
    """ A worker thread that takes directory names from a queue, finds all
        files in them recursively and reports the result.

        Input is done by placing directory names (as strings) into the
        Queue passed in dir_q.

        Output is done by placing tuples into the Queue passed in result_q.
        Each tuple is (thread name, dirname, [list of files]).

        Ask the thread to stop by calling its join() method.
    """
    def __init__(self, dataQueue, fichier):
        super(fillerWorker, self).__init__()
        self.dataQueue    = dataQueue        
        self.fichier     = open(fichier)

    def run(self):
        # As long as we weren't asked to stop, try to take new tasks from the
        # queue. The tasks are taken with a blocking 'get', so no CPU
        # cycles are wasted while waiting.
        # Also, 'get' is given a timeout, so stoprequest is always checked,
        # even if there's nothing in the queue.
   
            for i, line in enumerate(self.fichier):
                    #on prend ici une ligne de l'input et on le parse en numpy array avec 
                    #les channels qui nous interesse.
                    line = line.split(',')
                    line = [x.strip(' ') for x in line]
                    line = np.array(line)
                    line = line[0:8]
                    line = line.astype(np.float)
                    line[0] = i%1000
                    #le true ici peremet de s'assurer que la queue ne reste pas pleine trop longtemps
                    #il faudrait catch lerreur 
                    self.dataQueue.put(line, True)
                   


    def join(self, timeout=None):
        super(fillerWorker, self).join(timeout)
