
class QuickFind:

    def __init__(self, N):
        self._count = N  # number of components
        self.id = []    # id[i] = component identifier of i

        i = 0
        while i < N:
            self.id.append(i)
            i += 1


    def union(self,p , q):
        p_id = self.id[p] # needed for correctness
        q_id = self.id[q] # to reduce the number of array accesses

        # p and q are already in the same component
        if p_id == q_id:
            return

        for i in range(len(self.id)):
            if p_id == self.id[i]:
                self.id[i] = q_id

        self._count -= 1

    def find(self,p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self._count



## TEST ##
import fileinput

for line in fileinput.input():
    p_q = line.strip('\n').split(' ')

    # INIT
    if len(p_q) == 1:
        uf = QuickFind(int(p_q[0]))
        continue

    # Checks if they are connected
    if uf.connected(int(p_q[0]), int(p_q[1])):
        continue

    # union
    uf.union(int(p_q[0]), int(p_q[1]))
    print p_q

print uf.count()
