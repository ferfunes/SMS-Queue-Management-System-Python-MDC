class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        self._queue.append(item)
        return True
    def dequeue(self):
        return self._queue.pop(0) if self._mode == 'FIFO' else self._queue.pop()
    def get_queue(self):
       return self._queue
    def size(self):
        return len(self._queue) 


class example:
    def __init__(self,param1):
        self.x = param1
        

