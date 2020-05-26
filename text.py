# Shaishav Shah

"""
Text sprites for brick breaker
"""
from sprite import Sprite
from loader import *
from pygame import font


class Text(Sprite):

    def __init__(self,content,window, x= 0,y=0,fontFam = "Arial" ,fontsize = 24):
        Sprite.__init__(self,window,x,y)
        self.content = content
        self.fontFam = fontFam
        self.fontSize = fontsize
        self.color = WHITE
        self.font =  font.SysFont(self.fontFam, self.fontSize)
        self.sprite = self.font.render(self.content,1,self.color)

