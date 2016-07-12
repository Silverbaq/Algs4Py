class TopDownMerge:
    def sort(self, a):
        aux = [None] * len(a)
        self.sort2(a, aux, 0, len(a) - 1)
        return a

    def sort2(self, a, aux, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) / 2
        self.sort2(a, aux, lo, mid)
        self.sort2(a, aux, mid + 1, hi)
        self.merge(a, aux, lo, mid, hi)

    def merge(self, a, aux, lo, mid, hi):
        i = lo
        j = mid + 1

        # Copy a[lo...hi] to aux[lo..hi].
        for k in range(lo, hi + 1):
            aux[k] = a[k]

        # Merge back to a[lo..hi].
        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif less(aux[j], aux[i]):
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1


class ButtomUpMerge:
    def sort(self, a):
        n = len(a)
        aux = [None] * n

        l = 1
        while l < n:
            lo = 0
            while lo < n - l:
                mid = lo + l - 1
                hi = min(lo + l + l - 1, n - 1)
                self.merge(a, aux, lo, mid, hi)
                lo += l + l
            l *= 2
        return a

    def merge(self, a, aux, lo, mid, hi):
        # copy to aux[]
        for k in range(lo, hi + 1):
            aux[k] = a[k]

        # merge back to a[]
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif less(aux[j], aux[i]):
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1


# Helper functions
def less(v, w):
    return v < w


## TEST
a = [3, 1, 6, 4, 9, 7, 10, 5, 2]
m = TopDownMerge()
print m.sort(a)


b = [3, 1, 6, 4, 9, 7, 10, 5, 2]
bu = ButtomUpMerge()
print bu.sort(b)