
class Bag:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.first = None
        self.n = 0          # Number of elements in bag

    def add(self, item):
        old_first = self.first
        self.first = self.Node()
        self.first.data = item
        self.first.next = old_first
        self.n += 1

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.n




## TEST
b = Bag()
print "Size: %d" % b.size()
b.add("test")
print "Added element"
print "Size: %d" % b.size()
b.add("test")
print "Added element"
b.add("test")
print "Added element"
print "Size: %d" % b.size()
b.add("test")
print "Added element"
b.add("test")
print "Added element"
print "Size: %d" % b.size()