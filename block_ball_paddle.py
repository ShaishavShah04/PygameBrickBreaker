# 2020 - 05 - 25
# Shaishav Shah
from window import Window
from sprite import Sprite

class Block(Sprite):
    def __init__(self,window,height,width):
        Sprite.__init__(self,window)
        self.setDimensions(width,height)
        self.hit = False

    # ---
    def checkCollision(self, ball):
        if self.sprite.get_rect(x=self.x, y=self.y).colliderect(ball.getSprite().get_rect(x=ball.getX(), y=ball.getY())):
            self.hit = True
            return self.hit


class Ball(Sprite):
    def __init__(self,window,size):
        Sprite.__init__(self,window)
        self.setDimensions(size,size)
        self.dirX = 1
        self.dirY = 1
        self.speed = 5

    def bouncearound(self,frame):
        self.x += self.speed * self.dirX
        self.y += self.speed * self.dirY

        if self.x > frame.getWidth() - self.width:
            self.x = frame.getWidth() - self.width
            self.dirX = -1
        elif self.x < 0:
            self.x = 0
            self.dirX = 1
        #
        if self.y > frame.getHeight() - self.height:
            self.y = frame.getHeight() - self.height
            self.dirY = -1
        elif self.y < 0:
            self.y = 0
            self.dirY = 1
        #
        self.pos = (self.x, self.y)

    def bounceonce(self):
        self.dirX *= -1
        self.dirY *= -1

class Paddle(Sprite):
    def __init__(self,x,y,color):
        Sprite.__init__(self,window,x,y,color)
        self.speed = 10

    # -- Modify Methods

    def move(self,window,keys):

        if keys[K_d] == 1:
            self.x += self.speed
        if keys[K_a] == 1:
            self.x -= self.speed

        if self.x > window.getWidth() - self.sprite.get_rect().width:
            self.x = window.GgetHeight() - self.sprite.get_rect().width
        elif self.x < 0:
            self.x = 0

        self.pos = (self.x, self.y)







if __name__ == "__main__":
    from pygame import init
    init()

    window = Window()
    ball = Ball(window,5)
    ball.setPOS(200,200)
    block = Block(window,50,100)

    while True:
        window.getEvents()
        ball.bouncearound(window)
        if block.hit != True:
            if block.checkCollision(ball):
                ball.bounceonce()
                print("True")

        window.clearscreen()
        if block.hit != True:
            window.blitSprite(block)
        window.blitSprite(ball)
        window.updatescreen()
