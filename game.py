# Import a library of functions called 'pygame'
import pygame
import AStar
import graph as graphs
from graph import Graph
from graph import Node
import drawablenode
from drawablenode import *
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
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
# Set the height and width of the SCREEN

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SEARCH_SPACE = Graph([ROWS, COLS])

NODES = []
for i in range(ROWS):
    for j in range(COLS):
        node = SEARCH_SPACE.get_node([i, j])
        NODES.append(DrawableNode(node))

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
DONE = False
CLOCK = pygame.time.Clock()

pygame.font.init()
FONT1 = pygame.font.Font(None, 12)
FONT2 = pygame.font.Font(None, 28)
for n in NODES:
    for n_ in graphs.get_neighbors(n, SEARCH_SPACE):
        for nods in NODES:
            if n_.value[0] == nods.value[0] and n_.value[1] == nods.value[1]:
                n.adjacents.append(nods)
NODES[13].walkable = False
NODES[14].walkable = False
NODES[15].walkable = False
NODES[23].walkable = False
NODES[25].walkable = False
NODES[33].walkable = False

STARTNODE = NODES[0]
ENDNODE = NODES[24]

STARTNODE.start = True
ENDNODE.end = True

while not DONE:
    AStar.astar(STARTNODE, ENDNODE)
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    CLOCK.tick(1)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are DONE so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while DONE==False loop.

    # Clear the SCREEN and set the SCREEN background
    SCREEN.fill(WHITE)
    # Draw a circle
    for i in NODES:
        i.draw(SCREEN, FONT1)

    # Go ahead and update the SCREEN with what we've drawn.
    # This MUST happen after all the other drawing commands.
    BG = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    BG.fill(BLACK)
    TEXTRECT = BG.get_rect()
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
