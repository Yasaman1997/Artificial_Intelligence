import math


class Puzzle():

    def __init__(self, start, goal):

        self.goal = goal
        self.start = start
        self.state = []

    def blank(self, state):
        for i in range(0, len(state)):
            if state[i] == 0:
                return i + 1

    def actions(self, state):

        actions = []

        i = self.blank(state)
        row = math.ceil(i / 3)
        col = i % 3

        actions = ['r', 'u', 'l', 'd']
        if row == 1:
            if 'd' in actions:
                actions.remove('d')
        if row == 3:
            if 'u' in actions:
                actions.remove('u')
        if col == 1:
            if 'r' in actions:
                actions.remove('r')
        if col == 0:
            if 'l' in actions:
                actions.remove('l')

        return actions

    def result(self, state, action):
        i = self.blank(state)
        s = []
        if action == 'r':
            s = state[:]
            s[i - 1] = s[i - 2]
            s[i - 2] = 0
            newState = s[:]
        if action == 'l':
            s = state[:]
            s[i - 1] = s[i]
            s[i] = 0
            newState = s[:]
        if action == 'u':
            s = state[:]
            s[i - 1] = s[i + 2]
            s[i + 2] = 0
            newState = s[:]

        if action == 'd':
            s = state[:]
            s[i - 1] = s[i - 4]
            s[i - 4] = 0
            newState = s[:]

        return newState

    def goal_test(self, state):
        # print (state)
        return state == self.goal

    def cost(self, s1, s2):
        return 1

    def h_value(self, state):
        sqrt = 0
        i = state.index(1)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 1) ** (2.0) + (col - 1) ** (2.0)) ** (1 / 2.0)

        i = state.index(2)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 1) ** (2.0) + (col - 2) ** (2.0)) ** (1 / 2.0)

        i = state.index(3)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 1) ** (2.0) + (col - 3) ** (2.0)) ** (1 / 2.0)

        i = state.index(4)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 2) ** (2.0) + (col - 1) ** (2.0)) ** (1 / 2.0)

        i = state.index(5)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 2) ** (2.0) + (col - 2) ** (2.0)) ** (1 / 2.0)

        i = state.index(6)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 2) ** (2.0) + (col - 3) ** (2.0)) ** (1 / 2.0)

        i = state.index(7)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 3) ** (2.0) + (col - 1) ** (2.0)) ** (1 / 2.0)

        i = state.index(8)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 3) ** (2.0) + (col - 2) ** (2.0)) ** (1 / 2.0)

        i = state.index(0)
        row = math.ceil(i / 3)
        col = i % 3
        sqrt += ((row - 1) ** (2.0) + (col - 1) ** (2.0)) ** (1 / 2.0)

        return sqrt
