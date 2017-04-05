"""A*."""
import graph as G


def retrace(node):
    """Retrace Steps."""
    path = []
    iterator = node
    while iterator is not None:
        path.append(iterator)
        iterator = iterator.parent
    return path


def dist(curr, node):
    """Distance."""
    return 10 if curr.pos[0] == node.pos[0] or curr.pos[1] == node.pos[1] else 14


def mhd(node, goal):
    """Manhattan Distance."""
    return (abs(goal.pos[0] - node.pos[0]) + abs(goal.pos[1] - node.pos[1])) * 10


def astar(start, goal, graph):
    """AStar."""
    camefrom = []
    closed = []
    open_ = []
    start.h_cost = 0
    start.g_cost = 0
    start.f_cost = start.g_cost + start.h_cost
    open_.append(start)
    open_.sort(key=lambda x: x.f_cost)
    while len(open_) != 0:
        current = open_[0]
        open_.remove(current)
        closed.append(current)
        if current == goal:
            camefrom = retrace(current)
            return camefrom
        neighbors = G.get_neighbors(current, graph)
        for node in neighbors:
            if node in closed or node.walkable is False:
                continue
            tentative_g = current.g_cost + dist(current, node)
            if node not in open_:
                open_.append(node)
            elif tentative_g >= node.g_cost:
                continue
            node.parent = current
            node.g_cost = tentative_g
            node.h_cost = mhd(node, goal)
            node.f_cost = node.g_cost + node.h_cost

    return camefrom


if __name__ == '__main__':
    import game as Main
    Main.main()
