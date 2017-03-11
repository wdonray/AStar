'''graph.py'''


class Node(object):
    '''a node'''

    def __init__(self, value, identifier):
        self.__value = value
        self.__identifier = identifier

    @property
    def value(self):
        '''get value'''
        return self.__value

    @property
    def identifier(self):
        '''id'''
        return self.__identifier

    def print_info(self):
        '''get info'''
        print "ID:", self.__identifier, "Value:", self.__value


class Graph(object):
    '''the graph'''

    def __init__(self, dims):
        cols = dims[0]
        rows = dims[1]
        self._nodes = {}
        for i in range(0, cols):
            for j in range(0, rows):
                nodekey = str(i) + ',' + str(j)
                self._nodes[nodekey] = Node([i, j], len(self._nodes))

    def get_node(self, node):
        '''get a node by list [1,1]'''
        nodekey = str(node[0]) + ',' + str(node[1])
        if nodekey in self._nodes:
            return self._nodes[nodekey]


def get_neighbors(node, graph):
    '''get neighbors for a node'''

    right = [1, 0]
    top_right = [1, 1]

    top = [0, 1]
    top_left = [-1, 1]

    left = [-1, 0]
    bottom_left = [-1, -1]

    bottom = [0, -1]
    bottom_right = [1, -1]
    neighbors = []
    dirs = [right, top_right, top, top_left,
            left, bottom_left, bottom, bottom_right]

    for i in dirs:
        item1 = i[0] + node.value[0]
        item2 = i[1] + node.value[1]
        fetch_node = graph.get_node([item1, item2])
        if fetch_node:
            neighbors.append(fetch_node)
    return neighbors


def test_graph(graph):
    '''abc'''
    node = graph.get_node([1, 1])
    node.print_info()
    neighbors = get_neighbors(node, graph)
    for neighbor in neighbors:
        neighbor.print_info()

if __name__ == "__main__":
    test_graph(Graph([3, 3]))
