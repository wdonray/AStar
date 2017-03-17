"""The Game"""
import pygame
from AStarAlgo import PathFinding
import graph as graphs
from graph import Graph
from graph import Node
import drawablenode
from drawablenode import *

pygame.init()

MAROON = (128, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 20
COLS = 20
WIDTH = 30
HEIGHT = 30
SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SEARCH_SPACE = Graph([ROWS, COLS])


def nodedrawline(start, dest):
    """drawline"""
    pygame.draw.line(SCREEN, BLACK, (start.xpos,
                                     start.ypos), (dest.xpos, dest.ypos), 12)


NODES = []
COUNT = 0
mouse_listeners = []
for i in range(ROWS):  # Creates Rows and Cols and adds a node and a id to each
    for j in range(COLS):
        node = SEARCH_SPACE.get_node([i, j])
        n = DrawableNode(node, COUNT)
        NODES.append(n)
        mouse_listeners.append(n.printpos)
        COUNT += 1

pygame.display.set_caption("A Star Example Created By Donray Williams")

DONE = False
CLOCK = pygame.time.Clock()

pygame.font.init()

FONT = pygame.font.Font(None, 12)

for n in NODES:  # Creates Adjacents
    for n_ in graphs.get_neighbors(n, SEARCH_SPACE):
        for nods in NODES:
            if n_.value[0] == nods.value[0] and n_.value[1] == nods.value[1]:
                n.adjacents.append(nods)

# init the NODES
CURRENTNODE = NODES[0]
ENDNODE = NODES[ROWS * COLS - 1]
SELECTEDNODE = NODES[0]

PATH = []

Pathfinding_ = PathFinding()

while not DONE:

    CLOCK.tick(60)  # FPS
    pygame.mouse.set_cursor(*pygame.cursors.diamond)  # Useless Cursor

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        if event.type == pygame.KEYDOWN:

            # Begin Algorith (MemoryError: Error with created a certain amount
            # of starting points)
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                PATH = Pathfinding_.astar(CURRENTNODE, ENDNODE)
                for n in NODES:
                    n.parent = None
                    n.g_cost = 0
                    n.h_cost = 0
                    n.f_cost = 0

            # Move HightLighted Node right
            if (pygame.key.get_pressed()[pygame.K_RIGHT] and
                    SELECTEDNODE.identification + ROWS <= ROWS * COLS - 1):
                SELECTEDNODE = NODES[SELECTEDNODE.identification + ROWS]

             # Move HightLighted Node left
            if (pygame.key.get_pressed()[pygame.K_LEFT] and
                    SELECTEDNODE.identification - ROWS >= 0):
                SELECTEDNODE = NODES[SELECTEDNODE.identification - ROWS]

             # Move HightLighted Node up
            if (pygame.key.get_pressed()[pygame.K_UP] and
                    SELECTEDNODE.identification > 0):
                SELECTEDNODE = NODES[SELECTEDNODE.identification - 1]

            # Move HightLighted Node down
            if (pygame.key.get_pressed()[pygame.K_DOWN] and
                    SELECTEDNODE.identification < ROWS * COLS - 1):
                SELECTEDNODE = NODES[SELECTEDNODE.identification + 1]

            # Place starting node at pos of selected node
            if (pygame.key.get_pressed()[pygame.K_e] and
                    NODES[SELECTEDNODE.identification].walkable is True):
                CURRENTNODE = SELECTEDNODE

            # Place end node at pos of selected node
            if (pygame.key.get_pressed()[pygame.K_LSHIFT] and
                    NODES[SELECTEDNODE.identification].walkable is True):
                ENDNODE = SELECTEDNODE

            # Creates Walls
            if pygame.key.get_pressed()[pygame.K_w]:
                if NODES[SELECTEDNODE.identification].walkable is True:
                    NODES[SELECTEDNODE.identification].walkable = False
                elif NODES[SELECTEDNODE.identification].walkable is False:
                    NODES[SELECTEDNODE.identification].walkable = True

            # Clears Screen and sets Current, End, and Selected Node back to
            # original pos
            if pygame.key.get_pressed()[pygame.K_c]:
                for n in NODES:
                    n.walkable = True
                    n.parent = None
                    n.g_cost = 0
                    n.f_cost = 0
                    n.h_cost = 0
                    CURRENTNODE = NODES[0]
                    ENDNODE = NODES[ROWS * COLS - 1]
                    SELECTEDNODE = NODES[0]
            # Close Game
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                DONE = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            for callback in mouse_listeners:
                cb = callback(pygame.mouse.get_pos())
                if cb:
                    if event.button == 1:
                        CURRENTNODE = cb
                    elif event.button == 3:
                        ENDNODE = cb
                    elif event.button == 2:
                        PATH = Pathfinding_.astar(CURRENTNODE, ENDNODE)
                        for n in NODES:
                            n.parent = None
                            n.g_cost = 0
                            n.h_cost = 0
                            n.f_cost = 0


    SCREEN.fill(BLACK)  # Black Background

    # Draw all of the nodes
    for i in NODES:
        i.draw(SCREEN, FONT)

    # Draw Selected Node
    pygame.draw.rect(SCREEN, YELLOW,
                     [SELECTEDNODE.xpos, SELECTEDNODE.ypos, SELECTEDNODE.width,
                      SELECTEDNODE.height])

    # Draw Path
    if PATH is not None:
        for node in PATH:
            pygame.draw.rect(SCREEN, MAROON, pygame.Rect(
                node.xpos, node.ypos, node.width, node.height), 0)

    # Draw End Node
    pygame.draw.rect(SCREEN, RED,
                     [ENDNODE.xpos, ENDNODE.ypos, ENDNODE.width, ENDNODE.height])
    # Draw Start Node
    pygame.draw.rect(SCREEN, BLUE,
                     [CURRENTNODE.xpos, CURRENTNODE.ypos, CURRENTNODE.width, CURRENTNODE.height])

    #nodedrawline(CURRENTNODE, ENDNODE)

    BG = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    # BG.fill(BLACK)
    # TEXTRECT = BG.get_rect()
    pygame.display.flip()


pygame.quit()
