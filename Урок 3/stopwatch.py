import time

class Stopwatch(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Затраченное время: {:.3f} sec".format(time.time() - self._startTime))