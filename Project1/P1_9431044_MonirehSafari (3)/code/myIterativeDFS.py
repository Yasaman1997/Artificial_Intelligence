from myLimitedDFS import LIMITED_DFS


class ITERATIVE_DFS:
    def __init__(self, problem):
        self.f = []
        self.e = []
        self.problem = problem
        self.f.append(problem.start)

        self.path = []
        self.expand = []
        self.visited = []
        self.maxMemory = 0

    def ITlimitedDFSSearch(self):
        depth = 0
        ldfs = LIMITED_DFS(self.problem, depth)
        ldfs.limitedDFSSearch(0, 0)
        while (not ldfs.path):
            ldfs.path = []
            ldfs.e = []
            ldfs.limit = depth
            ldfs.limitedDFSSearch(self.problem.start, 0)
            depth += 1
            print(depth)
            self.path = ldfs.path
            self.visited = ldfs.visited
            self.expand = ldfs.expand

            self.maxMemory = ldfs.maxMemory
