class ASTAR:
    def __init__(self, problem):
        self.f = []
        self.e = []
        self.problem = problem
        self.f.append(problem.start)

        self.path = []
        self.expand = []
        self.visited = []
        self.maxMemory = 0

    def minInF(self) :

        min = self.f[0]
        for i in self.f:
            if i[1] < min[1]:
                min = i
        return min

    def ASTARSearch (self) :

        while self.f  :
            if len(self.f) + len(self.e) > self.maxMemory:
                self.maxMemory = len(self.f) + len(self.e)

            # print(self.f)
            a = self.minInF()
            p = a[0]
            if self.problem.goal_test(p[-1]):
                print("finish")
                self.path = p[:]
                return p

            if p[-1] not in self.visited :
                self.visited.append(p[-1])

            self.f.remove(a)
            self.e.append(p[-1])
            actions = self.problem.actions(p[-1])
            n = []
            for i in actions:
                n.append(self.problem.result(p[-1],i))
            for i in n:
                if (i not in self.e):
                    if i not in self.visited:
                        self.visited.append(i)
                    newp = p[:]
                    newp.append(i)
                    self.f.append([newp,(self.problem.cost(p[-1], i) + a[1] + self.problem.h_value(p[-1]))])

            self.expand = self.e
