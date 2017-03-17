import pygame
import AStar as PathFinding
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
ROWS = 15
COLS = 15
WIDTH = 30
HEIGHT = 30
SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SEARCH_SPACE = Graph([ROWS, COLS])

NODES = []
COUNT = 0
for i in range(ROWS):  # Creates Rows and Cols and adds a node and a id to each
    for j in range(COLS):
        node = SEARCH_SPACE.get_node([i, j])
        NODES.append(DrawableNode(node, COUNT))
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

CURRENTNODE = NODES[0]
ENDNODE = NODES[ROWS * COLS - 1]
SELECTEDNODE = NODES[0]
# init the NODES

while not DONE:

    CLOCK.tick(60)  # FPS 
    pygame.mouse.set_cursor(*pygame.cursors.diamond)  # Useless Cursor 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_RETURN]:  # Begin Algorith
                PathFinding.astar(CURRENTNODE, ENDNODE)
                for test in NODES:
                    if test.check is True:
                        test.check = False
                for x in PathFinding.retrace(ENDNODE):  # Draw the Path
                    x.check = True

            if pygame.key.get_pressed()[pygame.K_RIGHT] and SELECTEDNODE.identification + ROWS <= ROWS * COLS - 1: # Move HightLighted Node
                SELECTEDNODE = NODES[SELECTEDNODE.identification + ROWS]

            if pygame.key.get_pressed()[pygame.K_LEFT] and SELECTEDNODE.identification - ROWS >= 0: # Move HightLighted Node
                SELECTEDNODE = NODES[SELECTEDNODE.identification - ROWS]

            if pygame.key.get_pressed()[pygame.K_UP] and SELECTEDNODE.identification > 0:  # Move HightLighted Node
                SELECTEDNODE = NODES[SELECTEDNODE.identification - 1]

            if pygame.key.get_pressed()[pygame.K_DOWN] and SELECTEDNODE.identification < ROWS * COLS - 1:  # Move HightLighted Node
                SELECTEDNODE = NODES[SELECTEDNODE.identification + 1]

            if pygame.key.get_pressed()[pygame.K_e] and NODES[SELECTEDNODE.identification].walkable is True:  # Place starting node at pos of selected node
                for z in NODES:
                    if z.check is True:
                        z.check = False
                CURRENTNODE = SELECTEDNODE

            if pygame.key.get_pressed()[pygame.K_LSHIFT] and NODES[SELECTEDNODE.identification].walkable is True:  # Place end node at pos of selected node
                for x in NODES:
                    if x.check is True:
                        x.check = False
                ENDNODE = SELECTEDNODE

            if pygame.key.get_pressed()[pygame.K_w]: # Creates Walls 
                if NODES[SELECTEDNODE.identification].walkable is True:
                    NODES[SELECTEDNODE.identification].walkable = False
                    NODES[SELECTEDNODE.identification].check is False
                elif NODES[SELECTEDNODE.identification].walkable is False:
                    NODES[SELECTEDNODE.identification].walkable = True
                    NODES[SELECTEDNODE.identification].check is False

            if pygame.key.get_pressed()[pygame.K_c]:  # Clears Screen and sets Current, End, and Selected Node back to original pos
                for n in NODES:
                    n.walkable = True
                    n.parent = None
                    n.g_cost = 0
                    n.f_cost = 0
                    n.h_cost = 0
                    n.check = False
                    CURRENTNODE = NODES[0]
                    ENDNODE = NODES[ROWS * COLS - 1]
                    SELECTEDNODE = NODES[0]

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # Close Game
                DONE = True

    SCREEN.fill(BLACK)  # Black Background

    for i in NODES:
        i.draw(SCREEN, FONT)

    pygame.draw.rect(SCREEN, RED, [ENDNODE.xpos, ENDNODE.ypos, ENDNODE.width, ENDNODE.height])  # Draw End Node
    pygame.draw.rect(SCREEN, BLUE, [CURRENTNODE.xpos, CURRENTNODE.ypos, CURRENTNODE.width, CURRENTNODE.height])  # Draw Start Node
    pygame.draw.rect(SCREEN, YELLOW, [SELECTEDNODE.xpos, SELECTEDNODE.ypos, SELECTEDNODE.width, SELECTEDNODE.height])  # Draw Selected Node

    BG = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    # BG.fill(BLACK)
    # TEXTRECT = BG.get_rect()
    pygame.display.flip()

pygame.quit()
