# Shaishav Shah

"""
Text sprites for brick breaker
"""
from sprite import Sprite
from loader import *
from pygame import font


class Text(Sprite):

    def __init__(self,value,window, x= 0,y=0,phrase="",fontFam = "Arial" ,fontsize = 24,color=WHITE):
        Sprite.__init__(self,window,x,y)
        self.value = value
        self.phrase = phrase
        self.content = phrase + str(self.value) # For things such as "Level: X"
        self.fontFam = fontFam
        self.fontSize = fontsize
        self.color = color
        self.font =  font.SysFont(self.fontFam, self.fontSize)
        self.sprite = self.font.render(self.content,1,self.color)

    # Modify #-- Only for certain scenarios

    def add_to_Value(self):
        self.value += 1
        self.content = self.phrase + str(self.value)
        self.sprite = self.font.render(self.content,1,self.color)

    def remove_from_Value(self):
        self.value -= 1
        self.content = self.phrase + str(self.value)
        self.sprite = self.font.render(self.content,1,self.color)
    def change_value_to(self,value):
        self.value = value
        self.content = self.phrase + str(self.value)
        self.sprite = self.font.render(self.content, 1, self.color)
    # Getter

    def getvalue(self):
        return self.value