"""DrawableNode"""
import pygame


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
        self._gcost = 0
        self._hcost = 0
        self._fcost = 0

        # drawing vars
        size = 30
        self.width = size
        self.height = size
        self.identification = id
        self.index = (posx, posy)
        self.value = self.index
        self.xpos = (5 + self.width) * posx + 5
        self.ypos = (5 + self.height) * posy + 5
        self.pos = (self.width * posx, self.height * posy)
        self.screenpos = (self.xpos, self.ypos)
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
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
    def f_cost(self):
        """F Cost"""
        return self._fcost

    @property
    def g_cost(self):
        """G Cost"""
        return self._gcost

    @property
    def h_cost(self):
        """H Cost"""
        return self._hcost

    @f_cost.setter
    def f_cost(self, value):
        self._fcost = value

    @g_cost.setter
    def g_cost(self, value):
        self._gcost = value
        self._fcost = self._gcost + self._hcost

    @h_cost.setter
    def h_cost(self, value):
        self._hcost = value
        self._fcost = self._gcost + self._hcost

    @property
    def color(self):
        """Color"""
        return self._color

    @color.setter
    # manual setting of colors will mark them dirty so they will stay
    def color(self, value):
        red = (255, 0, 0)
        if value is red:
            self._color = value
            self.dirty = True
        else:
            self._color = value

        self._color = value

    def info(self):
        """Info Print"""
        print("pos = ", self.pos)
        ids = ""
        for i in self.adjacents:
            ids += " " + str(i.identification)
        print("neighbors:", ids)
        print("index: ", self.index)

    def draw(self, screen, font, init=True, text=True):
        """Draw"""
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
            textfpos = (self.xpos, self.ypos)  # top left
            textgpos = (self.xpos, self.ypos + self.height - 10)  # bot left

            # center it

            # draw the square
            if init and text:
                screen.blit(textf, textfpos)
                screen.blit(textg, textgpos)
