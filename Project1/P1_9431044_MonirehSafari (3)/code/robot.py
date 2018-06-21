class Robot():

    def __init__(self, start, goal, n, m, list):

        self.goal = goal
        self.start = start
        self.state = []
        self.n = n
        self.m = m
        self.list = list

    def actions(self, state):

        actions = ['r', 'u', 'l', 'd']
        if state[0] == 1:
            if 'u' in actions:
                actions.remove('u')
        if state[0] == self.n:
            if 'd' in actions:
                actions.remove('d')
        if state[1] == 1:
            if 'l' in actions:
                actions.remove('l')
        if state[1] == self.m:
            if 'r' in actions:
                actions.remove('r')

        for i in self.list:
            if state[0] == i[0] and state[1] == i[1]:
                if i[0] == i[2]:
                    if 'r' in actions:
                        actions.remove('r')
                if i[1] == i[3]:
                    if 'd' in actions:
                        actions.remove('d')
            if state[0] == i[2] and state[1] == i[3]:
                if i[0] == i[2]:
                    if 'l' in actions:
                        actions.remove('l')
                if i[1] == i[3]:
                    if 'u' in actions:
                        actions.remove('u')

        return actions

    def result(self, state, action):

        if action == 'r':
            newState = [state[0], state[1] + 1]
        if action == 'u':
            newState = [state[0] - 1, state[1]]
        if action == 'l':
            newState = [state[0], state[1] - 1]
        if action == 'd':
            newState = [state[0] + 1, state[1]]

        return newState

    def goal_test(self, state):
        # print (state)
        return state == self.goal

    def cost(self, s1, s2):
        return 1

    def h_value(self, s1):
        sqrt = ((s1[0] - self.goal[0]) ** (2.0) + (s1[1] - self.goal[1]) ** (2.0)) ** (1 / 2.0)
        return sqrt
