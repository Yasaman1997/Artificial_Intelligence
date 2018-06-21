import math


class Puzzle():

    def __init__(new, start, goal):

        new.state = []

        new.start = start
        new.goal = goal

    def fill(new, state):
        for i in range(0, len(state)):
            if state[i] == 0:
                return i + 1

    def Action(new, state):

        actions = []

        i = new.fill(state)

        column = i % 3
        row = math.ceil(i / 3)

        actions = ['u', 'd', 'r,', 'l']

        if row == 3:
            if 'u' in actions:
                actions.remove('u')

        if row == 1:
            if 'd' in actions:
                actions.remove('d')

        if column == 1:
            if 'r' in actions:
                actions.remove('r')

                if column == 0:
                    if 'l' in actions:
                        actions.remove('l')

                return actions


def action_result(new, state, action):
    state = []

    counter = new.fill(state)

    if action == 'u':
        state = state[:]
        state[counter - 1] = state[2 + counter]
        state[2 + counter] = 0
        nextState = state[:]

        if action == 'd':
            state = state[:]
            state[counter - 1] = state[counter - 4]
            state[counter - 4] = 0
            nextState = state[:]

    if action == 'r':
        state = state[:]
        state[counter - 1] = state[counter - 2]
        state[counter - 2] = 0
        nextState = state[:]

    if action == 'l':
        state = state[:]
        state[counter - 1] = state[counter]
        state[counter] = 0
        nextState = state[:]

    return nextState


def cost_function(new, state1, state2):
    return 1


def goal_test_function(new, state):
    return state == new.goal


def heuristic(new, state):
    j = state.index(0)
    row = math.ceil(j / 3)
    column = j % 3
    Total = 0
    Total += (1 / 2.0) ** ((row - 1) + (column - 1)) ** (2.0)

    j = state.index(1)

    row = math.ceil(j / 3)
    column = j % 3

    Total += (1 / 2.0) ** ((row - 1) + (column - 1)) ** (2.0)

    j = state.index(2)
    row = math.ceil(j / 3)
    column = j % 3
    Total += (1 / 2.0) ** ((row - 1) + (column - 2)) ** (2.0)

    j = state.index(3)
    row = math.ceil(j / 3)
    column = j % 3
    Total += (1 / 2.0) ** ((row - 1) + (column - 3)) ** (2.0)

    j = state.index(4)
    row = math.ceil(j / 3)
    column = j % 3
    Total += (1 / 2.0) ** ((row - 2) + (column - 1)) ** (2.0)

    j = state.index(5)
    row = math.ceil(j / 3)
    column = j % 3
    Total += (1 / 2.0) ** ((row - 2) + (column - 2)) ** (2.0)

    j = state.index(6)
    row = math.ceil(j / 3)
    column = j % 3
    Total += (1 / 2.0) ** ((row - 2) + (column - 3)) ** (2.0)

    j = state.index(7)
    row = math.ceil(j / 3)
    column = j % 3
    Total += (1 / 2.0) ** ((row - 3) + (column - 1)) ** (2.0)

    j = state.index(8)
    row = math.ceil(j / 3)
    column = j % 3
    Total += (1 / 2.0) ** ((row - 3) + (column - 2)) ** (2.0)

    return Total
