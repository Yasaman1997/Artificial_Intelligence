class G:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]