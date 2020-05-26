# Shaishav Shah

"""
Abstract class for all sprites
"""
from pygame import Surface, SRCALPHA

class Sprite:

    def __init__(self,window,x = 0, y = 0,color = (255,255,255)):
        self.width = 100
        self.height = 100
        self.dimensions = (self.width,self.height)
        self.sprite = Surface(self.dimensions,SRCALPHA, 32)
        self.color = color
        self.sprite.fill(self.color)
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.window = window

    # -- Modify

    def updateSprite(self):
        self.dimensions = (self.width, self.height)
        self.sprite = Surface(self.dimensions, SRCALPHA, 32)
        self.sprite.fill(self.color)

    def setWidth(self, w):
        self.width = w
        self.updateSprite()

    def setHeight(self,h):
        self.height = h
        self.updateSprite()

    def setColor(self,color):
        self.color = color

    def setDimensions(self,w,h):
        self.width = w
        self.height = h
        self.updateSprite()

    def setX(self,x):
        self.x = x
        self.pos = (self.x, self.y)

    def setY(self,y):
        self.y = y
        self.pos = (self.x, self.y)

    def setPOS(self,x,y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    # -- Getter

    def getSprite(self):
        return self.sprite

    def getPOS(self):
        return self.pos

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getX(self):
        return self.x

    def getY(self):
        return self.y
