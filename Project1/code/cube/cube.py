class Cube():

    def __init__(self, start, goal):

        self.goal = goal
        self.start = start
        self.state = []

    def actions(self, state):

        actions = ['T', 'TC', 'F', 'FC', 'R', 'RC']
        return actions

    def actionResult(self, state, action):

        new_state = state[:]

        if action == 'T':
            new_state[0] = state[2]
            new_state[1] = state[0]
            new_state[2] = state[3]
            new_state[3] = state[1]
            new_state[4] = state[20]
            new_state[5] = state[21]
            new_state[6] = state[6]
            new_state[7] = state[7]
            new_state[8] = state[8]
            new_state[9] = state[9]
            new_state[10] = state[10]
            new_state[11] = state[11]
            new_state[12] = state[12]
            new_state[13] = state[13]
            new_state[14] = state[16]
            new_state[15] = state[17]
            new_state[16] = state[4]
            new_state[17] = state[5]
            new_state[18] = state[18]
            new_state[19] = state[19]
            new_state[20] = state[15]
            new_state[21] = state[14]
            new_state[22] = state[22]
            new_state[23] = state[23]

        if action == 'TC':
            new_state[0] = state[1]
            new_state[1] = state[3]
            new_state[2] = state[0]
            new_state[3] = state[2]
            new_state[4] = state[16]
            new_state[5] = state[17]
            new_state[6] = state[6]
            new_state[7] = state[7]
            new_state[8] = state[8]
            new_state[9] = state[9]
            new_state[10] = state[10]
            new_state[11] = state[11]
            new_state[12] = state[12]
            new_state[13] = state[13]
            new_state[14] = state[21]
            new_state[15] = state[20]
            new_state[16] = state[14]
            new_state[17] = state[15]
            new_state[18] = state[18]
            new_state[19] = state[19]
            new_state[20] = state[4]
            new_state[21] = state[5]
            new_state[22] = state[22]
            new_state[23] = state[23]

        if action == 'F':
            new_state[0] = state[2]
            new_state[1] = state[0]
            new_state[2] = state[19]
            new_state[3] = state[17]
            new_state[4] = state[6]
            new_state[5] = state[4]
            new_state[6] = state[7]
            new_state[7] = state[5]
            new_state[8] = state[22]
            new_state[9] = state[20]
            new_state[10] = state[10]
            new_state[11] = state[11]
            new_state[12] = state[12]
            new_state[13] = state[13]
            new_state[14] = state[16]
            new_state[15] = state[17]
            new_state[16] = state[4]
            new_state[17] = state[8]
            new_state[18] = state[18]
            new_state[19] = state[9]
            new_state[20] = state[2]
            new_state[21] = state[14]
            new_state[22] = state[3]
            new_state[23] = state[23]

        if action == 'FC':

            new_state[0] = state[2]
            new_state[1] = state[0]
            new_state[2] = state[20]
            new_state[3] = state[22]
            new_state[4] = state[5]
            new_state[5] = state[7]
            new_state[6] = state[4]
            new_state[7] = state[6]
            new_state[8] = state[17]
            new_state[9] = state[19]
            new_state[10] = state[10]
            new_state[11] = state[11]
            new_state[12] = state[12]
            new_state[13] = state[13]
            new_state[14] = state[16]
            new_state[15] = state[17]
            new_state[16] = state[4]
            new_state[17] = state[3]
            new_state[18] = state[18]
            new_state[19] = state[2]
            new_state[20] = state[9]
            new_state[21] = state[21]
            new_state[22] = state[8]
            new_state[23] = state[23]

            if action == 'R':
                new_state[0] = state[0]
                new_state[1] = state[5]
                new_state[2] = state[2]
                new_state[3] = state[7]
                new_state[4] = state[4]
                new_state[5] = state[9]
                new_state[6] = state[6]
                new_state[7] = state[11]
                new_state[8] = state[8]
                new_state[9] = state[13]
                new_state[10] = state[10]
                new_state[11] = state[15]
                new_state[12] = state[12]
                new_state[13] = state[1]
                new_state[14] = state[14]
                new_state[15] = state[3]
                new_state[16] = state[16]
                new_state[17] = state[17]
                new_state[18] = state[18]
                new_state[19] = state[19]
                new_state[20] = state[21]
                new_state[21] = state[23]
                new_state[22] = state[20]
                new_state[23] = state[22]

                if action == 'RC':
                    new_state[0] = state[0]
                    new_state[1] = state[13]
                    new_state[2] = state[2]
                    new_state[3] = state[15]
                    new_state[4] = state[4]
                    new_state[5] = state[1]
                    new_state[6] = state[6]
                    new_state[7] = state[3]
                    new_state[8] = state[8]
                    new_state[9] = state[5]
                    new_state[10] = state[10]
                    new_state[11] = state[7]
                    new_state[12] = state[12]
                    new_state[13] = state[9]
                    new_state[14] = state[14]
                    new_state[15] = state[11]
                    new_state[16] = state[16]
                    new_state[17] = state[17]
                    new_state[18] = state[18]
                    new_state[19] = state[19]
                    new_state[20] = state[22]
                    new_state[21] = state[20]
                    new_state[22] = state[23]
                    new_state[23] = state[21]

        return new_state


def goal_test_function(new, state):
    for i in range(0, 6):
        if not (state[0 + i * 4] == state[3 + i * 4]) | (
                state[0 + i * 4] == state[1 + i * 4] and state[0 + i * 4] == state[2 + i * 4]):
            return False

    return True

    def cost_function(self, state1, state2):
        return 1

    def heuristic(self, state):
        return 1
