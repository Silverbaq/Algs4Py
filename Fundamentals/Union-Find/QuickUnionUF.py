class QuickUnion:

    def __init__(self, N):
        self._count = N  # number of components
        self.parent = []

        i = 0
        while i < N:
            self.parent.append(i)
            i += 1

    def count(self):
        return self._count

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        self.parent[root_p] = root_q
        self._count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p is not self.parent[p]:
            p = self.parent[p]
        return p




## TEST ##
import fileinput

for line in fileinput.input():
    p_q = line.strip('\n').split(' ')

    # INIT
    if len(p_q) == 1:
        uf = QuickUnion(int(p_q[0]))
        continue

    # Checks if they are connected
    if uf.connected(int(p_q[0]), int(p_q[1])):
        continue

    # union
    uf.union(int(p_q[0]), int(p_q[1]))
    print p_q

print uf.count()
