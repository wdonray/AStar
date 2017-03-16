import pygame
import AStar
import graph as graphs
from graph import Graph
from graph import Node
import drawablenode
from drawablenode import *

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 10
COLS = 10
WIDTH = 30
HEIGHT = 30
SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SEARCH_SPACE = Graph([ROWS, COLS])

NODES = []
for i in range(ROWS):
    for j in range(COLS):
        node = SEARCH_SPACE.get_node([i, j])
        NODES.append(DrawableNode(node))

pygame.display.set_caption("Example code for the draw module")

DONE = False
CLOCK = pygame.time.Clock()

pygame.font.init()

FONT = pygame.font.Font(None, 12)

for n in NODES:
    for n_ in graphs.get_neighbors(n, SEARCH_SPACE):
        for nods in NODES:
            if n_.value[0] == nods.value[0] and n_.value[1] == nods.value[1]:
                n.adjacents.append(nods)

NODES[11].walkable = False
NODES[12].walkable = False
NODES[13].walkable = False
NODES[14].walkable = False
NODES[15].walkable = False
NODES[16].walkable = False
NODES[21].walkable = False
NODES[31].walkable = False
NODES[41].walkable = False
NODES[51].walkable = False
NODES[61].walkable = False


while not DONE:
    CURRENTNODE = NODES[0]
    ENDNODE = NODES[99]
    SELECTEDNODE = NODES[0]
    
    CURRENTNODE.start = True
    ENDNODE.end = True

    CLOCK.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                AStar.astar(CURRENTNODE, ENDNODE)
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                DONE = True
    for x in AStar.retrace(ENDNODE):
        x.check = True

    SCREEN.fill(BLACK)
    for i in NODES:
        i.draw(SCREEN, FONT)

    BG = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    BG.fill(BLACK)
    TEXTRECT = BG.get_rect()
    pygame.display.flip()

pygame.quit()
