# 2020 - 05 - 25
# Shaishav Shah

"""
Classes for block, paddle, and ball

Things shown:
- Inheritance from abstract class sprite
- Polymorphism: Getter Methods return different results based on object. Eg. Object.getX() != Object2.getX()
- Encapsulation: self.__hit. This is a private variable and can only be accessed via the class functions

Note:
    In all my collision testings, the range of acceptance is + / - the ball's speed as without it, some bounces will not be registed
"""

from window import Window
from sprite import Sprite
from pygame import K_d, K_a, K_s, K_w, K_SPACE
from loader import GREEN
from random import randrange

class Block(Sprite):
    def __init__(self,window,height,width):
        Sprite.__init__(self,window)
        self.setDimensions(width,height)
        self.__hit = False # Variable to see if it is hit or not

    # -- Modify Method
    def blockmoves(self, level,direction): # For the shake effect in level 2
        if level > 1:
            self.setPOS(self.getX()+(direction*2), self.getY())

    """
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
        """ # Old collisions

    # Modify Methods

    def getHit(self):
        self.__hit = True

    # Getter Methods

    def checkCollision(self, ball): # (Overall getter methods apart from the self.getHit()

        # Collisions
        if self.getRect().colliderect(ball.getRect()): # If any overlap between block and ball
            self.getHit() # Set block to disappear
            # Variables inside if-statement to save memory
            t_l = (ball.getX(), ball.getY())  # Top left corner
            t_r = (ball.getX() + ball.getWidth(), ball.getY())
            b_r = (ball.getX() + ball.getWidth(), ball.getY() + ball.getHeight())
            b_l = (ball.getX(), ball.getY() + ball.getHeight())
            # Collision testing

            if t_l[0] >= (self.getX() + self.getWidth() - ball.speed) and b_l[0] >= (self.getX() + self.getWidth() - ball.speed) and t_l[1] <= (self.getY()+ self.getHeight()+ball.speed) and b_l[1] >= (self.getY() - ball.speed): # Left edge collision
                return 1 # Left
            elif t_r[0] <= (self.getX()+ball.speed) and b_r[0] <= (self.getX()+ball.speed) and t_r[1] <= (self.getY()+ self.getHeight()+ball.speed) and b_r[1] >= (self.getY() - ball.speed):
                return 1 # Right
            else:
                return 2 # Top/Bottom

    def checkHit(self):
        return self.__hit


class Ball(Sprite):

    def __init__(self,window,size):
        Sprite.__init__(self,window)
        self.setDimensions(size,size)
        self.dirX = randrange(-1,2,2) # Randomize direction
        self.dirY = -1
        self.speed = 5

    # Modify Methods

    def moveWASD(self,keypresses): # USED for testing
        if keypresses[K_d] == 1:
            self.x += self.speed
        if keypresses[K_a] == 1:
            self.x -= self.speed

        if keypresses[K_w] == 1:
            self.y -= self.speed
        if keypresses[K_s] == 1:
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


    def bouncearound(self,bounce): # Standard bouncing around function... nothing interesting
                                    # Bounce is returned to indicate whether ball has touched floor or not
        self.x += self.speed * self.dirX
        self.y += self.speed * self.dirY

        if self.x > self.window.getWidth() - self.width:
            self.x = self.window.getWidth() - self.width
            self.dirX = -1
        elif self.x < 0:
            self.x = 0
            self.dirX = 1
        #
        if self.y >= self.window.getHeight() - self.height:
            self.y = self.window.getHeight() - self.height
            self.dirY = -1
            return -1 # Look at description above

        elif self.y < 0:
            self.y = 0
            self.dirY = 1
        #
        self.pos = (self.x, self.y)
        return bounce # Bounce explained above

    def bouncehorizontal(self):
        self.dirX *= -1

    def bouncevertical(self):
        self.dirY *= -1

    def bounceboth(self): # May implement for corners... But I think it would make it look bad... and the chances of ball hitting the corner exactly are small
        self.bouncevertical()
        self.bouncehorizontal()

    def setmiddle(self): # For restarts / new level / life lost
        self.setPOS(self.window.getWidth()/2 - self.getWidth()/2 , randrange(530,561,1))

    def randomdirection(self): # After restart
        self.dirX = randrange(-1, 2, 2) # Either Left or Right
        self.dirY = -1


class Paddle(Sprite):
    def __init__(self, window,color):
        Sprite.__init__(self,window,color=color)
        self.speed = 10
        self.setDimensions(100,10)
        self.setPOS(self.window.getWidth()/2 - self.getWidth()/2, self.window.getHeight() - (2 * self.height))

    # -- Modify Methods

    def move(self,keys): # Only left / Right movement

        if keys[K_d] == 1:
            self.x += self.speed
        if keys[K_a] == 1:
            self.x -= self.speed

        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x < 0:
            self.x = 0

        self.pos = (self.x, self.y)

    # -- Getter Methods

    def checkCollision(self,ball):
        if self.sprite.get_rect(x=self.x, y=self.y).colliderect(ball.getSprite().get_rect(x=ball.getX(), y=ball.getY())): # If overlap
            #
            b_r = (ball.getX() + ball.getWidth(), ball.getY() + ball.getHeight())
            b_l = (ball.getX(), ball.getY() + ball.getHeight())
            #
            if b_l[0] <= (self.getX()+self.getWidth()) and b_r[0] >= self.getX() and b_l[1] <= self.getY() + ball.speed: # and if ball is on top of the paddle
                return 1 # Bounce vertically
            else:
                return 2 # Bounce horizontally
        else:
            return 0 # Don't bounce





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
            block.checkCollision(ball)
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
