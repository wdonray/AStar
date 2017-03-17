"""DrawableNode"""
import pygame


class DrawableNode(object):
    '''drawable node'''

    def __init__(self, graphnode, ident):
        posx = graphnode.value[0]
        posy = graphnode.value[1]
        self.adjacents = []
        self.parent = None
        self._walkable = True
        self._check = False
        self._gcost = 0
        self._hcost = 0
        self._fcost = 0

        size = 30
        self.width = size
        self.height = size
        self.identification = ident
        self.index = (posx, posy)
        self.value = self.index
        self.xpos = (5 + self.width) * posx + 5
        self.ypos = (5 + self.height) * posy + 5
        self.pos = (self.width * posx, self.height * posy)
        self.screenpos = (self.xpos, self.ypos)
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height))
        self._color = (102, 255, 102)

    @property
    def check(self):
        """check"""
        return self._check

    @check.setter
    def check(self, value):
        maroon = (128, 0, 0)
        self._check = value
        if value is False:
            self.color = (102, 255, 102)
        else:
            self.color = maroon

    @property
    def walkable(self):
        """walkable"""
        return self._walkable

    @walkable.setter
    def walkable(self, value):
        black = (0, 0, 0)
        self._walkable = value
        if value:
            self.color = (102, 255, 102)
        else:
            self.color = black

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
    def color(self, value):
        red = (255, 0, 0)
        if value is red:
            self._color = value
        else:
            self._color = value

        self._color = value

    def draw(self, screen, font, init=True, text=True):
        """Draw"""
        self.surface.fill(self._color)
        screen.blit(self.surface, self.screenpos)
        """"if self.walkable:

            textf = font.render("P " + str(self.index), True, (1, 1, 1))
            textg = font.render(
                "ID " + str(self.identification), True, (1, 1, 1))

            textfpos = (self.xpos, self.ypos)  # top left
            textgpos = (self.xpos, self.ypos + self.height - 10)  # bot left

            if init and text:
                screen.blit(textf, textfpos)
                screen.blit(textg, textgpos)"""
