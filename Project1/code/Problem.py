class Problem(object):

    def __init__(new, initial_state, goal):
        new.initial = initial_state
        new.goal = goal

        def action(new, state):
            raise NotImplementedError

        def action_result(new, state, action):
            raise NotImplementedError

    def goal_test_function(new, state):
        raise NotImplementedError

    def cost_function(new, cost, state1, action, state2):
        return cost + 1

    def heuristic(new, state):
        raise NotImplementedError
