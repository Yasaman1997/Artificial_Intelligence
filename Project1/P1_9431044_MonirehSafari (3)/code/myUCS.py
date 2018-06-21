class UCS:
    def __init__(self, problem):
        self.f = []
        self.e = []
        self.problem = problem
        self.f.append(problem.start)
        self.act = []
        self.path = []
        self.expand = []
        self.visited = []
        self.maxMemory = 0

    def minInF(self):
        min = self.f[0]
        for i in self.f:
            if i[1] < min[1]:
                min = i
        return min

    def UCSSearch(self):

        while self.f:
            if len(self.f) + len(self.e) > self.maxMemory:
                self.maxMemory = len(self.f) + len(self.e)

            a = self.minInF()
            p = a[0]
            if self.problem.goal_test(p[-1]):
                self.path = p[:]
                print("finish")
                return p

            self.f.remove(a)
            if p[-1] not in self.e:
                self.e.append(p[-1])

            actions = self.problem.actions(p[-1])
            n = []
            for i in actions:
                n.append(self.problem.result(p[-1], i))
            for i in n:
                if i not in self.e:
                    self.visited.append(i)
                    newp = p[:]
                    newp.append(i)
                    self.f.append([newp, (self.problem.cost(a, i) + a[1])])

            self.expand = self.e
