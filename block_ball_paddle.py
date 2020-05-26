# 2020 - 05 - 25
# Shaishav Shah
from window import Window
from sprite import Sprite
from pygame import K_a, K_d
from loader import GREEN

class Block(Sprite):
    def __init__(self,window,height,width):
        Sprite.__init__(self,window)
        self.setDimensions(width,height)
        self.hit = False

    # -- Getter Method
    def checkCollision(self, ball):
        if self.sprite.get_rect(x=self.x, y=self.y).colliderect(ball.getSprite().get_rect(x=ball.getX(), y=ball.getY())):
            self.hit = True
        # Find border which it touched... Since ball could bounce either vertical or horizontal
            if ball.getX() == (self.getX() + self.getWidth()) or (ball.getX() + ball.getWidth()) == self.getX():
                # horizontal bounce ^
                return 1# "1" means horizontal
            else:
                return 2



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

    def bouncehorizontal(self):
        self.dirX *= -1

    def bouncevertical(self):
        self.dirY *= -1

    def bounceboth(self):
        self.bouncevertical()
        self.bouncehorizontal()


class Paddle(Sprite):
    def __init__(self, window,color):
        Sprite.__init__(self,window,color=color)
        self.speed = 10
        self.setDimensions(100,10)
        self.setPOS(self.window.getWidth()/2 - self.getWidth()/2, self.window.getHeight() - (2 * self.height))

    # -- Modify Methods

    def move(self,keys):

        if keys[K_d] == 1:
            self.x += self.speed
        if keys[K_a] == 1:
            self.x -= self.speed

        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x < 0:
            self.x = 0

        self.pos = (self.x, self.y)

    def checkCollision(self,ball):
        return self.sprite.get_rect(x=self.x, y=self.y).colliderect(ball.getSprite().get_rect(x=ball.getX(), y=ball.getY()))






if __name__ == "__main__":
    from pygame import init
    init()

    window = Window()
    ball = Ball(window,5)
    ball.setPOS(200,200)
    block = Block(window,50,100)
    block.setPOS(550,500)
    paddle = Paddle(window,GREEN)
    bounce = 0


    while True:
        window.getEvents()
        #
        ball.bouncearound(window)
        if not block.hit:
            bounce = block.checkCollision(ball)
            if block.hit:
                if bounce == 1:
                    ball.bouncehorizontal()
                else:
                    ball.bouncevertical()

        paddle.move(window.getKeys())
        if paddle.checkCollision(ball):
            ball.bouncevertical()

        window.clearscreen()
        if not block.hit:
            window.blitSprite(block)
        window.blitSprite(paddle)
        window.blitSprite(ball)
        window.updatescreen()
