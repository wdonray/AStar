'''A*'''


def retrace(node):
    '''Retrace Steps'''
    path = []
    while node.parent is not None:
        path.append(node)
        node = node.parent
    return path


def dist(curr, node):
    '''Distance'''
    return 10 if curr.index[0] == node.index[0] or curr.index[1] == node.index[1] else 14


def mhd(node, goal):
    '''Manhattan Distance'''
    return (abs(goal.index[0] - node.index[0]) + abs(goal.index[1] - node.index[1])) * 10


def astar(start, goal):
    '''AStar'''
    camefrom = []
    closed = []
    open_ = []
    start.h_cost = 0
    start.g_cost = 0
    start.f_cost = start.g_cost + start.h_cost
    open_.append(start)
    while open_ is not None:
        open_ = sorted(open_, key=lambda x: x.f_cost)
        current = open_[0]
        open_.remove(current)
        closed.append(current)
        if current == goal:
            camefrom = retrace(current)
            return camefrom
        for node in current.adjacents:
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
