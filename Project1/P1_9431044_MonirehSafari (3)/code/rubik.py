class Rubik():

    def __init__(self, start, goal):

        self.goal = goal
        self.start = start
        self.state = []

    def actions(self, state):

        actions = ['R', 'T', 'TC', 'F', 'FC', 'RC']
        return actions

    def result(self, state, action):
        newState = []
        newState = state[:]
        if action == 'RC':
            newState[0] = state[0]
            newState[1] = state[13]
            newState[2] = state[2]
            newState[3] = state[15]
            newState[4] = state[4]
            newState[5] = state[1]
            newState[6] = state[6]
            newState[7] = state[3]
            newState[8] = state[8]
            newState[9] = state[5]
            newState[10] = state[10]
            newState[11] = state[7]
            newState[12] = state[12]
            newState[13] = state[9]
            newState[14] = state[14]
            newState[15] = state[11]
            newState[16] = state[16]
            newState[17] = state[17]
            newState[18] = state[18]
            newState[19] = state[19]
            newState[20] = state[22]
            newState[21] = state[20]
            newState[22] = state[23]
            newState[23] = state[21]
        if action == 'R':
            newState[0] = state[0]
            newState[1] = state[5]
            newState[2] = state[2]
            newState[3] = state[7]
            newState[4] = state[4]
            newState[5] = state[9]
            newState[6] = state[6]
            newState[7] = state[11]
            newState[8] = state[8]
            newState[9] = state[13]
            newState[10] = state[10]
            newState[11] = state[15]
            newState[12] = state[12]
            newState[13] = state[1]
            newState[14] = state[14]
            newState[15] = state[3]
            newState[16] = state[16]
            newState[17] = state[17]
            newState[18] = state[18]
            newState[19] = state[19]
            newState[20] = state[21]
            newState[21] = state[23]
            newState[22] = state[20]
            newState[23] = state[22]

        if action == 'T':
            newState[0] = state[2]
            newState[1] = state[0]
            newState[2] = state[3]
            newState[3] = state[1]
            newState[4] = state[20]
            newState[5] = state[21]
            newState[6] = state[6]
            newState[7] = state[7]
            newState[8] = state[8]
            newState[9] = state[9]
            newState[10] = state[10]
            newState[11] = state[11]
            newState[12] = state[12]
            newState[13] = state[13]
            newState[14] = state[16]
            newState[15] = state[17]
            newState[16] = state[4]
            newState[17] = state[5]
            newState[18] = state[18]
            newState[19] = state[19]
            newState[20] = state[15]
            newState[21] = state[14]
            newState[22] = state[22]
            newState[23] = state[23]

        if action == 'TC':
            newState[0] = state[1]
            newState[1] = state[3]
            newState[2] = state[0]
            newState[3] = state[2]
            newState[4] = state[16]
            newState[5] = state[17]
            newState[6] = state[6]
            newState[7] = state[7]
            newState[8] = state[8]
            newState[9] = state[9]
            newState[10] = state[10]
            newState[11] = state[11]
            newState[12] = state[12]
            newState[13] = state[13]
            newState[14] = state[21]
            newState[15] = state[20]
            newState[16] = state[14]
            newState[17] = state[15]
            newState[18] = state[18]
            newState[19] = state[19]
            newState[20] = state[4]
            newState[21] = state[5]
            newState[22] = state[22]
            newState[23] = state[23]

        if action == 'F':
            newState[0] = state[2]
            newState[1] = state[0]
            newState[2] = state[19]
            newState[3] = state[17]
            newState[4] = state[6]
            newState[5] = state[4]
            newState[6] = state[7]
            newState[7] = state[5]
            newState[8] = state[22]
            newState[9] = state[20]
            newState[10] = state[10]
            newState[11] = state[11]
            newState[12] = state[12]
            newState[13] = state[13]
            newState[14] = state[16]
            newState[15] = state[17]
            newState[16] = state[4]
            newState[17] = state[8]
            newState[18] = state[18]
            newState[19] = state[9]
            newState[20] = state[2]
            newState[21] = state[14]
            newState[22] = state[3]
            newState[23] = state[23]

        if action == 'FC':
            newState[0] = state[2]
            newState[1] = state[0]
            newState[2] = state[20]
            newState[3] = state[22]
            newState[4] = state[5]
            newState[5] = state[7]
            newState[6] = state[4]
            newState[7] = state[6]
            newState[8] = state[17]
            newState[9] = state[19]
            newState[10] = state[10]
            newState[11] = state[11]
            newState[12] = state[12]
            newState[13] = state[13]
            newState[14] = state[16]
            newState[15] = state[17]
            newState[16] = state[4]
            newState[17] = state[3]
            newState[18] = state[18]
            newState[19] = state[2]
            newState[20] = state[9]
            newState[21] = state[21]
            newState[22] = state[8]
            newState[23] = state[23]

        return newState

    def goal_test(self, state):
        for i in range(0, 6):
            if not state[0 + i * 4] == state[3 + i * 4]:
                return False
            if not (state[0 + i * 4] == state[1 + i * 4] and state[0 + i * 4] == state[2 + i * 4]):
                return False
        return True

    def cost(self, s1, s2):
        return 1

    def h_value(self, state):
        return 1
