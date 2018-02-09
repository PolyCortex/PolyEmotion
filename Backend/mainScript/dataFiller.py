import time
import threading, Queue

class fillerWorker(threading.Thread):
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
        self.dataQueue = dataQueue        
        self.stoprequest = threading.Event()
        with open(fichier) as self.fichier

    def run(self):
        # As long as we weren't asked to stop, try to take new tasks from the
        # queue. The tasks are taken with a blocking 'get', so no CPU
        # cycles are wasted while waiting.
        # Also, 'get' is given a timeout, so stoprequest is always checked,
        # even if there's nothing in the queue.
        while not self.stoprequest.isSet():
            try:
                for i, line in enumerate(self.fichier):
                    if i > 5:
                        line = line.split(',')
                        ch2 = float(line[2])
                        queue.put(ch2,timeout=0.05)
                        queue.task_done()
            except Queue.Empty:
                continue

    def join(self, timeout=None):
        self.stoprequest.set()
        super(fillerWorker, self).join(timeout)
