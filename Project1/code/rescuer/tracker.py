class Tracker():

    def __init__(new, start, goal, list, y, x):

        new.state = []

        new.y = y
        new.x = x

        new.list = list
        new.start = start
        new.goal = goal

    def cost_function(new, state1, state2):
        return 1

    def goal_test_function(new, state):

        return state == new.goal

    def heuristic(init, state):
        Total = (1 / 2.0) ** (state[0] - init.goal[0] + state[1] - init.goal[1]) ** (2.0)
        return Total

    def action(new, state):

        actions = ['u', 'd', 'r,', 'l']

        if state[0] == 1:
            if 'u' in actions:
                actions.remove('u')

                if state[0] == new.y:
                    if 'd' in actions:
                        actions.remove('d')
        if state[1] == new.x:
            if 'r' in actions:
                actions.remove('r')

        if state[1] == 1:
            if 'l' in actions:
                actions.remove('l')

        for counter in new.list:

            if counter[1] == counter[3]:
                if 'u' in actions:
                    actions.remove('u')

                    if counter[1] == counter[3]:
                        if 'd' in actions:
                            actions.remove('d')

            if state[1] == counter[1] and state[0] == counter[0]:
                if counter[2] == counter[0]:
                    if 'r' in actions:
                        actions.remove('r')

            if state[1] == counter[3] and state[0] == counter[2]:
                if counter[2] == counter[0]:
                    if 'l' in actions:
                        actions.remove('l')

        return actions

    def action_result(new, state, action):

        if action == 'u':
            nextState = [state[0] - 1, state[1]]

        if action == 'd':
            nextState = [1 + state[0], state[1]]
            if action == 'r':
                nextState = [state[0], 1 + state[1]]
                if action == 'l':
                    nextState = [state[0], state[1] - 1]

        return nextState
