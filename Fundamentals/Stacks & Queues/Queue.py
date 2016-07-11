
class Queue:



    def __init__(self):
        self.first = None    # beginning of queue
        self.last = None     # end of queue
        self.n = 0           # Number of elements in the queue

    def enqueue(self, item):
        oldLast = self.last
        self.last = self.Node()
        self.last.data = item
        self.last.next = None

        if self.isEmpty():
            self.first = self.last
        else:
            oldLast.next = self.last
        self.n += 1

    def dequeue(self):
        item = self.first.data
        self.first = self.first.next
        self.n -= 1

        if self.isEmpty():
            self.last = None
        return item

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.n




## TEST
q = Queue()
q.enqueue("test")
q.enqueue("test2")
print q.dequeue()
print q.dequeue()
q.enqueue("test3")
print q.dequeue()
q.enqueue("test4")
print q.dequeue()