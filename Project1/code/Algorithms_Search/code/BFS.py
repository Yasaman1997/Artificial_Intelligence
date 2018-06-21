class BFS:

    def __init__(self, problem):
        self.f = []
        self.e = []
        self.path = []
        self.f.append(problem.start)
        self.problem = problem

        self.path = []
        self.expand = []
        self.visited = []
        self.Mem = 0

    def bfsSearch (self) :

        while self.f:

            if len(self.f) + len(self.e) > self.Mem :
                self.Mem = len(self.f) + len(self.e)

            a = self.f[0]
            p = a[0]
            if self.problem.goal_function(p[-1]):
                print("finish")
                self.path = p[:]
                return p

            self.f.remove(a)
            self.e.append(p[-1])

            actions = self.problem.action(p[-1])
            n = []
            for i in actions:
                n.append(self.problem.action_result(p[-1], i))
            for i in n:
                if i not in self.e:
                    if i not in self.visited :
                        self.visited.append(i)
                    newp = p[:]
                    newp.append(i)
                    self.f.append([newp])

        self.expand = self.e

