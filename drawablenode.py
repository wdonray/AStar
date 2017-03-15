import pygame
import math
import graph
from graph import Graph
from graph import Node


class DrawableNode(object):
    '''drawable node'''

    def __init__(self, graphnode):
        # astar vars
        posx = graphnode.value[0]
        posy = graphnode.value[1]
        self.adjacents = []
        self.parent = None
        self._walkable = True
        self._start = False
        self._end = False
        self._check = False
        self._g = 0
        self._h = 0
        self._f = 0

        # drawing vars
        SIZE = 30
        self.width = SIZE
        self.height = SIZE
        self.id = id
        self.index = (posx, posy)
        self.value = self.index
        self.x = (5 + self.width) * posx + 5
        self.y = (5 + self.height) * posy + 5
        self.pos = (self.width * posx, self.height * posy)
        self.screenpos = (self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height))
        self.dirty = False
        self._color = (125, 255, 255)

    # properties

    @property
    def check(self):
        """check"""
        return self._check

    @check.setter
    def check(self, value):
        white = (255, 255, 255)
        maroon = (128, 0, 0)
        self._check = value
        if value is False:
            self.color = white
        else:
            self.color = maroon

    @property
    def start(self):
        """start"""
        return self._start

    @start.setter
    def start(self, value):
        white = (255, 255, 255)
        green = (0, 255, 0)
        self._start = value
        if value is False:
            self.color = white
        else:
            self.color = green

    @property
    def end(self):
        """end"""
        return self._end

    @end.setter
    def end(self, value):
        white = (255, 255, 255)
        blue = (0, 203, 254)
        self._end = value
        if value is False:
            self.color = white
        else:
            self.color = blue

    @property
    def walkable(self):
        """walkable"""
        return self._walkable

    @walkable.setter
    def walkable(self, value):
        white = (255, 255, 255)
        red = (255, 0, 0)
        self._walkable = value
        # if it's set to walkable change to white
        # this will mark it as undirty
        if value:
            self.color = white
        else:
            self.color = red

    @property
    def f(self):
        return self._f

    @property
    def g(self):
        return self._g

    @property
    def h(self):
        return self._h

    @f.setter
    def f(self, value):
        self._f = value

    @g.setter
    def g(self, value):
        self._g = value
        self._f = self._g + self._h

    @h.setter
    def h(self, value):
        self._h = value
        self._f = self._g + self._h

    @property
    def color(self):
        return self._color

    @color.setter
    # manual setting of colors will mark them dirty so they will stay
    def color(self, value):
        white = (255, 255, 255)
        red = (255, 0, 0)

        if value is red:
            self._color = value
            self.dirty = True
        else:
            self._color = value

        self._color = value

    def info(self):
        print("pos = ", self.pos)
        ids = ""
        for i in self.adjacents:
            ids += " " + str(i.id)
        print("neighbors:", ids)
        print("index: ", self.index)

    def draw(self, screen, font, init=True, text=True):
        # pygame.draw.rect(screen, self._color, self.rect)
        self.surface.fill(self._color)
        screen.blit(self.surface, self.screenpos)
        if self.walkable:
            # create some text to go on the fill

            # info to display

            # render the text

            textf = font.render("P= " + str(self.index), True, (1, 1, 1))
            textg = font.render("" + str(), True, (1, 1, 1))

            # set it's position/parent
            textfpos = (self.x, self.y)  # top left
            textgpos = (self.x, self.y + self.height - 10)  # bot left

            # center it

            # draw the square
            if init and text:
                screen.blit(textf, textfpos)
                screen.blit(textg, textgpos)
