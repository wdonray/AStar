'''A*'''


def retrace(node):
    '''Retrace Steps'''


def dist(curr, node):
    '''Distance'''


def mhd(node, goal):
    '''Manhattan Distance'''
    return abs(goal.xpos - node.xpos) + abs(goal.ypos - node.ypos) * 10

def astar(start, goal):
    '''AStar'''
    camefrom = []
    closed = []
    open = []
    start.h = 0
    start.g = 0
    start.f = start.g + start.h
    open.append(start)
    while open is not None:
        sorted(open, key=lambda x: x.f)
        current = open[0]
        if current == goal:
            camefrom = retrace(current)
            break
        for node in current.adjacents:
            if node in closed or node.notwalkable:
                continue
            tentative_g = node.g + dist(current, node)
            if node not in open:
                open.append(node)
            elif tentative_g >= node.g:
                continue
            node.parent = current
            node.g = tentative_g
            node.f = node.g + mhd(node, goal)
