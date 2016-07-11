
class Stack:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.first = None   # First element in Stack
        self.n = 0          # Number of elements in Stack

    def push(self, item):
        old_first = self.first
        self.first = self.Node()
        self.first.data = item
        self.first.next = old_first
        self.n += 1

    def pop(self):
        item = self.first.data
        self.first = self.first.next
        self.n -= 1
        return item

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.n



## TEST
s = Stack()
print "Stack size: %d" % s.size()
s.push("TEST")
print "Added element to stack"
print "Stack size: %d" % s.size()
s.push("TEST2")
print "Added element to stack"
print "Stack size: %d" % s.size()
print "Popping element %s" % s.pop()
print "Stack size: %d" % s.size()
s.push("TEST3")
print "Added element to stack"
print "Stack size: %d" % s.size()
print "Popping element %s" % s.pop()
print "Stack size: %d" % s.size()
s.push("TEST4")
print "Added element to stack"
print "Stack size: %d" % s.size()
print "Popping element %s" % s.pop()
print "Stack size: %d" % s.size()
print "Popping element %s" % s.pop()
print "Stack size: %d" % s.size()