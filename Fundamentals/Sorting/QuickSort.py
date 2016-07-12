from random import shuffle

class Quick:
    def sort(self, a):
        shuffle(a) # a needs to be in random order
        return self.sort2(a, 0, len(a) - 1)

    def sort2(self, a, lo, hi):
        if hi <= lo:
            return
        j = self.partition(a, lo, hi)
        self.sort2(a, lo, j - 1)  # Sort left part a[lo .. j-1]
        self.sort2(a, j + 1, hi)  # Sort right part a[j+1 .. hi]
        return a

    def partition(self, a, lo, hi):
        # Partition into a[lo .. i-1], a[i], a[i+1 .. hi]
        i = lo  # left and right scan indices
        j = hi + 1
        v = a[lo]  # partitioning item
        while True:
            # Scan right, scan left, check for scan complete, and exchange.
            i += 1
            while self.less(a[i], v): # Find item on lo to swap
                if i is hi:
                    break
                i += 1

            j -= 1
            while self.less(v, a[j]): # Find item on hi to swap
                if j is lo:
                    break
                j -= 1

            if i >= j:
                break
            self.exch(a, i, j)  # Put v = a[j] into position

        self.exch(a, lo, j) # Put partitioning item v at a[j]
        return j  # with a[lo .. j-1] <= a[j] <= a[j+1 .. hi]

    def less(self, v, w):
        return v < w

    def exch(self, a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp


## TEST
a = [3, 1, 6, 4, 9, 7, 10, 5]
m = Quick()
print m.sort(a)

b = [3, 1, 6, 11, 545, 123, 323, 4, 9, 7, 42, 33, 102, 10, 5]
print m.sort(b)

c = ['c', 'b', 'a']
print m.sort(c)
