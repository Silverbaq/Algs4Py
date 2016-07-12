class Selection:
    def sort(self, a):
        n = len(a)  # Length of the array

        # Sorting a into increasing order.
        for i in range(n):
            # Exchange a[i] with smallest entry in a[i+1...N]
            min = i

            for j in range(i+1, n):
                if less(a[j], a[min]):
                    min = j
            exch(a, i, min)
        return a


class Insertion:
    def sort(self, a):
        n = len(a)
        for i in range(n):
            j = i
            while j > 0 and less(a[j], a[j-1]):
                exch(a, j, j-1)
                j-=1
        return a


class Shell:
    def sort(self, a):
        n = len(a)
        # 3x+1 increment sequence:  1, 4, 13, 40, 121, 364, 1093, ...
        h = 1
        while h < n/3:
            h = 3*h + 1

        while h >= 1:
            # h-sort the array
            for i in range(h, n):
                j = i
                while j >= h and less(a[j], a[j-h]):
                    exch(a, j, j-h)
                    j-=h
            h /= 3
        return a


# Helper functions
def less(v, w):
    return v < w


def exch(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def isSorted(a):
    for i in range(1,len(a)):
        if less(a[i], a[i-1]):
            return False
    return True


## TEST Selection
s = Selection()
a = [2,3,6,4,10,1]
print s.sort(a)

i = Insertion()
a2 = [2,3,6,4,10,1]
print i.sort(a2)

h = Shell()
a3 = [2,3,6,4,10,1]
print h.sort(a3)