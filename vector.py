'''Simple vector classes'''
import math

class Vector2(object):
    '''Simple Vector 2D math class'''
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def magnitude(self):
        '''Returns the magnitude of the vector'''
        return math.sqrt((self.xpos * self.xpos) + (self.ypos * self.ypos))

    def normalize(self):
        '''Returns a unit vector'''
        if self.magnitude() == 0:
            return Vector2(self.xpos / 1, self.ypos / 1)
        else:
            return Vector2(self.xpos / self.magnitude(), self.ypos / self.magnitude())

    def scale(self, scalar):
        '''Scales the value of the vector'''
        return Vector2(self.xpos * scalar, self.ypos * scalar)

    def __add__(self, rhs):
        return Vector2(rhs.xpos + self.xpos, rhs.ypos + self.ypos)

    def __sub__(self, rhs):
        return Vector2(self.xpos - rhs.xpos, self.ypos - rhs.ypos)

    def __eq__(self, rhs):
        return rhs.xpos == self.xpos and rhs.ypos == self.ypos

    def __ne__(self, rhs):
        return rhs.xpos == self.xpos and rhs.ypos == self.ypos

    def __div__(self, rhs):
        return Vector2(self.xpos / rhs, self.ypos / rhs)

    def __mul__(self, rhs):
        return Vector2(self.xpos * rhs.xpos, self.ypos * rhs.ypos)

    def __str__(self):
        return "<" + str(self.xpos) + "," + str(self.ypos) + ">"
