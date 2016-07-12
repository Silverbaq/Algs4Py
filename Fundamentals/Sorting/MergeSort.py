class TopDownMerge:

    def sort(self, a):
        aux = [None] * len(a)
        self.sort2(a, aux, 0, len(a)-1)
        return a

    def sort2(self, a, aux, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) / 2
        self.sort2(a, aux, lo, mid)
        self.sort2(a, aux, mid + 1, hi)
        merge(a, aux, lo, mid, hi)


class ButtomUpMerge:
    def sort(self, a):

        pass


def merge(a, aux, lo, mid, hi):
    i = lo
    j = mid +1

    # Copy a[lo...hi] to aux[lo..hi].
    for k in range(lo, hi+1):
        aux[k] = a[k]

    # Merge back to a[lo..hi].
    for k in range(lo, hi+1):
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
a = [3,1,6,4,9,7,10,5,2]
m = TopDownMerge()
print m.sort(a)