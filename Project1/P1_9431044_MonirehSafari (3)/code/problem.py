class Problem(object):

    def __init__(self, initial, goal=None):

        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        raise NotImplementedError

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h_value(self, state):
        raise NotImplementedError




