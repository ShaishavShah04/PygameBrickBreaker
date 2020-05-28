# 2020 - 05 - 25
# Shaishav Shah
from window import Window
from sprite import Sprite
import pygame
from loader import GREEN
from random import randrange

class Block(Sprite):
    def __init__(self,window,height,width):
        Sprite.__init__(self,window)
        self.setDimensions(width,height)
        self.hit = False

    # -- Modify Method
    def blockmoves(self, level,direction):
        if level > 1:
            self.setPOS(self.getX()+(direction*3), self.getY())

    def checkCollision(self,ball):
        if self.sprite.get_rect(x=self.x, y=self.y).colliderect(ball.getSprite().get_rect(x=ball.getX(), y=ball.getY())):
            self.hit = True
            print(ball.getX(),self.getX(),self.getX()+self.getWidth())
            # Border Find
            if self.getX()+5 >= ball.getX() >= (self.getX() - 10): # Left edge
                print('l')
                return 1
            elif (self.getX()+self.getWidth()-10) <= ball.getX() <= (self.getX()+self.getWidth()+5): # Right edge
                print('r')
                return 1
            else:
                print("Top/bottom")
                return 2

    def checkCollision2(self,ball):


        # Collisions
        if self.getRect().colliderect(ball.getRect()): # If any overlap between block and ball

            # Variables inside if-statement to save memory
            t_l = (ball.getX(), ball.getY())  # Top left corner
            t_r = (ball.getX() + ball.getWidth(), ball.getY())
            b_r = (ball.getX() + ball.getWidth(), ball.getY() + ball.getHeight())
            b_l = (ball.getX(), ball.getY() + ball.getHeight())
            # Collision testing
            if t_l[0] >= (self.getX() + self.getWidth() - 5) and b_l[0] >= (self.getX() + self.getWidth() - 5) and t_l[1] <= (self.getY()+ self.getHeight()+5) and b_l[1] >= (self.getY() - 5): # Left edge collision
                print("Left")
                return 1
            elif t_r[0] <= (self.getX()+5) and b_r[0] <= (self.getX()+5) and t_r[1] <= (self.getY()+ self.getHeight()+5) and b_r[1] >= (self.getY() - 5):
                print("Right")
                return 1
            else:
                print("Top or bottom")
                return 2













    # -- Getter Method
    def checkHit(self):
        return self.hit



class Ball(Sprite):
    def __init__(self,window,size):
        Sprite.__init__(self,window)
        self.setDimensions(size,size)
        self.dirX = randrange(-1,2,2)
        self.dirY = randrange(-1,2,2)
        self.speed = 1

    def moveWASD(self,keypresses):
        if keypresses[pygame.K_d] == 1:
            self.x += self.speed
        if keypresses[pygame.K_a] == 1:
            self.x -= self.speed

        if keypresses[pygame.K_w] == 1:
            self.y -= self.speed
        if keypresses[pygame.K_s] == 1:
            self.y += self.speed

        # chk x
        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x < 0:
            self.x = 0

        # Chk y
        if self.y > self.window.getHeight() - self.sprite.get_rect().height:
            self.y = self.window.getHeight() - self.sprite.get_rect().height
        elif self.y < 0:
            self.y = 0
        self.pos = (self.x, self.y)

    def bounceEverywhere(self, frame):
        self.x += self.DirX * self.spd
        self.y += self.DirY * self.spd
        #
        if self.x > frame.GetVW() - self.width:
            self.x = frame.GetVW() - self.width
            self.DirX = -1
        elif self.x < 0:
            self.x = 0
            self.DirX = 1
        #
        if self.y > frame.GetVH() - self.height:
            self.y = frame.GetVH() - self.height
            self.DirY = -1
        elif self.y < 0:
            self.y = 0
            self.DirY = 1
        #
        self.pos = (self.x, self.y)




    def bouncearound(self,bounce):

        self.x += self.speed * self.dirX
        self.y += self.speed * self.dirY

        if self.x > self.window.getWidth() - self.width:
            self.x = self.window.getWidth() - self.width
            self.dirX = -1
        elif self.x < 0:
            self.x = 0
            self.dirX = 1
        #
        if self.y > self.window.getHeight() - self.height:
            self.y = self.window.getHeight() - self.height
            self.dirY = -1
            return -1
        elif self.y < 0:
            self.y = 0
            self.dirY = 1
        #
        self.pos = (self.x, self.y)
        return bounce

    def bouncehorizontal(self):
        self.dirX *= -1

    def bouncevertical(self):
        self.dirY *= -1

    def bounceboth(self):
        self.bouncevertical()
        self.bouncehorizontal()

    def setmiddle(self):
        self.setPOS(self.window.getWidth()/2 - self.getWidth()/2 , 550)

    def randomdirection(self):
        self.dirX = randrange(-1, 2, 2) # Either Left or Right
        self.dirY = -1

class Paddle(Sprite):
    def __init__(self, window,color):
        Sprite.__init__(self,window,color=color)
        self.speed = 10
        self.setDimensions(100,10)
        self.setPOS(self.window.getWidth()/2 - self.getWidth()/2, self.window.getHeight() - (2 * self.height))

    # -- Modify Methods

    def move(self,keys):

        if keys[pygame.K_d] == 1:
            self.x += self.speed
        if keys[pygame.K_a] == 1:
            self.x -= self.speed

        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x < 0:
            self.x = 0

        self.pos = (self.x, self.y)

    def checkCollision(self,ball):
        return self.sprite.get_rect(x=self.x, y=self.y).colliderect(ball.getSprite().get_rect(x=ball.getX(), y=ball.getY()))






if __name__ == "__main__": # Confirming stuff works with one block
    from pygame import init
    init()

    window = Window()
    ball = Ball(window,10)
    ball.setPOS(700,400)
    block = Block(window,50,100)
    block.setPOS(550,500)
    paddle = Paddle(window,GREEN)
    bounce = 0


    while True:
        window.getEvents()
        #
        ball.moveWASD(window.getKeys())
        #bounce = ball.bouncearound(bounce)
        if not block.hit:
            block.checkCollision2(ball)
            if block.hit:
                if bounce == 1:
                    ball.bouncehorizontal()
                else:
                    ball.bouncevertical()

        # paddle.move(window.getKeys())
        if paddle.checkCollision(ball):
            ball.bouncevertical()

        window.clearscreen()
        if not block.hit:
            window.blitSprite(block)
        window.blitSprite(paddle)
        window.blitSprite(ball)
        window.updatescreen()
