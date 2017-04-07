"""Graph."""


class Node(object):
    """Node Class."""

    def __init__(self, value, identifier):
        """__init__."""
        self.value = value
        self.identifier = identifier

    @property
    def value(self):
        """Get value."""
        return self.value

    @property
    def identifier(self):
        """Return ID."""
        return self.identifier

    def print_info(self):
        """Get info."""
        print "ID:", self.identifier, "Value:", self.value


class Graph(object):
    """Graph Class."""

    def __init__(self, dims):
        """__init__."""
        cols = dims[0]
        rows = dims[1]
        self.nodes = {}
        for i in range(0, cols):
            for j in range(0, rows):
                nodekey = str(i) + ',' + str(j)
                self.nodes[nodekey] = Node([i, j], len(self.nodes))

    def get_node(self, node):
        """Get a node by list [1,1]."""
        nodekey = str(node[0]) + ',' + str(node[1])
        if nodekey in self.nodes:
            return self.nodes[nodekey]


def get_neighbors(node, graph):
    """Get neighbors for a node."""
    current = node
    right = (current[0] + 1, current[1])
    top_right = (current[0] + 1, current[1] - 1)

    top = (current[0], current[1] - 1)
    top_left = (current[0] - 1, current[1] - 1)

    left = (current[0] - 1, current[1])
    bottom_left = (current[0] - 1, current[1] + 1)

    bottom = (current[0], current[1] + 1)
    bottom_right = (current[0] + 1, current[1] + 1)

    directions = [right, top_right, top, top_left,
                  left, bottom_left, bottom, bottom_right]
    neighbors = []
    for i in graph:
        node = (i[0], i[1])
        if node in directions:
            neighbors.append(i)
    return neighbors


if __name__ == '__main__':
    import game as Main
    Main.main()
