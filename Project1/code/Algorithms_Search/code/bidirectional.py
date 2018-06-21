class bidirectional:

    def __init__(self, problem):
        self.f1 = []
        self.f2 = []
        self.e1 = []
        self.e2 = []
        self.p1 = []
        self.p2 = []

        self.init = []

        self.f1.append(problem.start)
        self.f2.append(problem.goal)
        self.problem = problem
        self.goal = problem.goal
        self.turn = True

        self.path = []
        self.expand = []
        self.visit = []
        self.Mem = 0


def bidirectSearch(self):

        while (not self.finish()):

            while self.f1 and self.turn:

                if len(self.f1) + len(self.f2) + len(self.e1) + len(self.e2) > self.Mem:
                    self.Mem = len(self.f1) + len(self.f2) + len(self.e1) + len(self.e2)

                a = self.f1[0]
                self.p1 = a[0]
                if self.problem.goal_function(self.p1[-1]):
                    print("finish")
                    return self.p1

                self.f1.remove(a)
                self.e1.append(self.p1[-1])

                actions = self.problem.action(self.p1[-1])
                n = []
                for i in actions:
                    n.append(self.problem.action_result(self.p1[-1], i))
                for i in n:
                    if i not in self.e1:
                        newp = self.p1[:]
                        newp.append(i)
                        self.f1.append([newp])
                        if self.p1[-1] not in self.visit:
                            self.visit.append(self.p1[-1])
                self.turn = not self.turn

            while self.f2 and (not self.turn):

                a = self.f2[0]
                self.p2 = a[0]
                if self.problem.goal_function(self.p2[-1]):
                    print("finish")
                    return self.p2

                self.f2.remove(a)
                self.e2.append(self.p2[-1])

                actions = self.problem.action(self.p2[-1])
                n = []
                for i in actions:
                    n.append(self.problem.action_result(self.p2[-1], i))
                for i in n:
                    if i not in self.e2:
                        newp = self.p2[:]
                        newp.append(i)
                        self.f2.append([newp])
                        if self.p2[-1] not in self.visit:
                            self.visit.append(self.p2[-1])
                self.turn = not self.turn

        for i in self.p1:
            if (not i in self.init):
                self.path.append(i)
            else:
                break

        for i in reversed(self.p2):
            if (not i in self.init):
                self.p2.remove(i)
            else:
                break

        class bidirectional:

            def __init__(self, problem):
                self.f1 = []
                self.f2 = []
                self.e1 = []
                self.e2 = []
                self.p1 = []
                self.p2 = []
                self.common = []
                self.f1.append(problem.start)
                self.f2.append(problem.goal)
                self.problem = problem
                self.goal = problem.goal
                self.turn = True

                self.path = []
                self.expand = []
                self.visited = []
                self.maxMemory = 0

            def finish(self):
                for i in self.p1:

                    if i in self.p2:
                        print(self.p1)
                        print(self.p2)
                        print(i)
                        self.common.append(i)
                        return True

            def biSearch(self):

                while (not self.finish()):

                    while self.f1 and self.turn:

                        if len(self.f1) + len(self.f2) + len(self.e1) + len(self.e2) > self.maxMemory:
                            self.maxMemory = len(self.f1) + len(self.f2) + len(self.e1) + len(self.e2)

                        a = self.f1[0]
                        self.p1 = a[0]
                        if self.problem.goal_function(self.p1[-1]):
                            print("finish")
                            return self.p1

                        self.f1.remove(a)
                        self.e1.append(self.p1[-1])

                        actions = self.problem.action(self.p1[-1])
                        n = []
                        for i in actions:
                            n.append(self.problem.action_result(self.p1[-1], i))
                        for i in n:
                            if i not in self.e1:
                                newp = self.p1[:]
                                newp.append(i)
                                self.f1.append([newp])
                                if self.p1[-1] not in self.visited:
                                    self.visited.append(self.p1[-1])
                        self.turn = not self.turn

                    while self.f2 and (not self.turn):

                        a = self.f2[0]
                        self.p2 = a[0]
                        if self.problem.goal_function(self.p2[-1]):
                            print("finish")
                            return self.p2

                        self.f2.remove(a)
                        self.e2.append(self.p2[-1])

                        actions = self.problem.action(self.p2[-1])
                        n = []
                        for i in actions:
                            n.append(self.problem.action_result(self.p2[-1], i))
                        for i in n:
                            if i not in self.e2:
                                newp = self.p2[:]
                                newp.append(i)
                                self.f2.append([newp])
                                if self.p2[-1] not in self.visited:
                                    self.visited.append(self.p2[-1])
                        self.turn = not self.turn

                for i in self.p1:
                    if (not i in self.common):
                        self.path.append(i)
                    else:
                        break

                for i in reversed(self.p2):
                    if (not i in self.common):
                        self.p2.remove(i)
                    else:
                        break

                for i in reversed(self.p2):
                    self.path.append(i)

                self.expand = self.e1[:]
                for i in self.e2:
                    if i not in self.expand:
                        self.expand.append(i)

        for i in reversed(self.p2):
            self.path.append(i)

        self.expand = self.e1[:]
        for i in self.e2:
            if i not in self.expand:
                self.expand.append(i)



def finish(self):
        for i in self.p1:

            if i in self.p2:
                print(i)
                self.init.append(i)

                print(self.p1)
                print(self.p2)


                return True






