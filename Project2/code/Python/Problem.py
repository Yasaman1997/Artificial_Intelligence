class Problem(object):

    def __init__(new, initial_state, goal):
        new.initial = initial_state
        new.goal = goal

        def neighbour(new, state):
            raise NotImplementedError

        def action_result(new, state, action):
            raise NotImplementedError

    def goal_function(new, state):
        raise NotImplementedError
