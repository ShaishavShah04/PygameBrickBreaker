# Shaishav Shah
# 2020-05-26
"""
Engine for gluing all the things togather... This will also incorporate levels

Things Shown:
- Aggregation: When creating class of ball, paddle, and text, they mostly use self.window as a parameter.
"""

from window import Window
from block_ball_paddle import Block, Ball, Paddle
from text import Text
from loader import *
from pygame import K_SPACE, K_y

class Game:

    def __init__(self):
        # Variables
        self.window = Window()
        self.ball = Ball(self.window, 15)
        self.ball.setmiddle()  # setting ball in starting spot
        self.player = Paddle(self.window, BLACK) # Preset into middle

        self.onscreen = [] # Array of blocks which are on the screen ( Not hit yet )

        # Text and Positions which I had to do manually since centering technique didnt work for me

        self.lives = Text(LIVES,self.window,phrase="Lives: ",color=GREEN) # Aggregation
        self.lives.setPOS(self.window.getWidth() - self.lives.getWidth(), 10) # Top right
        self.score = Text(0,self.window,10,self.window.getHeight() - 30,"Score: ",color=RED)
        self.title = Text("Brick-Breaker!",self.window,fontsize=18)
        self.title.setPOS(self.window.getWidth()/2 - self.title.getWidth()/2, 10)
        self.level = Text(0,self.window,2,10,"Level: ",color=BLUE)
        self.introtext = Text("Press Space To Start!",self.window, self.window.getWidth()/2 - 90,300)
        self.halt = Text("Life Lost!!! Press Space to Continue!",self.window)
        self.halt.setPOS(self.window.getWidth()/2 - self.halt.getWidth() - 50, self.window.getHeight()/2 - self.halt.getHeight()/2)
        self.gameover = Text("Game Over!",self.window,fontsize=36)
        self.gameover.setPOS(self.window.getWidth() / 2 - self.gameover.getWidth()/2 - 20 ,self.window.getHeight() / 2 - self.gameover.getHeight() / 2)
        self.nextlevel = Text("Press Space for next level",self.window)
        self.nextlevel.setPOS(self.window.getWidth()/2 - self.nextlevel.getWidth() , self.window.getHeight() - (2*self.nextlevel.getHeight()))
        self.gameoveroptions = Text("Press SPACE or Y to play again",self.window)
        self.gameoveroptions.setPOS(self.window.getWidth()/2 - self.gameoveroptions.getWidth()/2 - 100, self.window.getHeight() - (4*self.gameoveroptions.getHeight()/2))


        # Creating Blocks
        self.createblocks()

        # All the little things that are on / off screen .... Misc = miscellaneous
        self.misc = [self.ball, self.player, self.title, self.level,self.score,self.lives, self.introtext]

    # Modifier

    def intro(self):
        if self.chkspace(self.window.getKeys()):
            self.misc.pop()
            self.level.add_to_Value()

    def createblocks(self):
        for i in range(6):
            for j in range(6):
                temp_starting_array = [100, 50]
                temp_starting = temp_starting_array[i%2]
                self.onscreen.append(Block(self.window,50,100))
                self.onscreen[-1].setPOS(temp_starting + (j * 105) ,60 + (i*55))
                self.onscreen[-1].setColor(blockcolors[i])

    def run(self):
        ## Var
        halt = False
        max_move = 15
        move = [-1,1]
        next_level = False
        gameOn = True

        while True:


            ## Variables
            bounce = 0
            ## Inputs
            self.window.getEvents()

            ## Processing
            if self.level.getvalue() == 0  and self.lives.getvalue() != 0: # Start Game
                self.intro()

            elif self.level.getvalue() != 0 and self.lives.getvalue() == 0: # Game Over

                self.misc = [self.ball, self.player, self.title, self.level,self.score,self.lives, self.gameover,self.gameoveroptions]

                if self.chkspace(self.window.getKeys()) or self.chk_y(self.window.getKeys()): # Play again
                    # Reset variables
                    self.misc.pop()
                    self.misc.pop()
                    self.onscreen = []
                    self.createblocks()
                    self.ball.setmiddle()
                    self.player.setPOS(self.window.getWidth() / 2 - self.player.getWidth() / 2, self.window.getHeight() - (2 * self.player.height))
                    halt = False
                    next_level = False
                    self.level.change_value_to(1)
                    self.score.change_value_to(0)
                    self.lives.change_value_to(3)
                    continue

            elif self.level.getvalue() >= 1 and self.lives.getvalue() > 0: # Levels / Gameplay

                if halt: # After losing life, just a pause
                    self.misc = [self.ball, self.player, self.title, self.level,self.score,self.lives, self.halt]
                    if self.chkspace(self.window.getKeys()):
                        self.ball.randomdirection()
                        self.misc = [self.ball, self.player, self.title, self.level,self.score,self.lives]
                        halt = False

                elif next_level:
                    self.player.setDimensions(100 - (20*self.level.getvalue()),10)
                    self.player.setPOS(self.window.getWidth() / 2 - self.player.getWidth() / 2, self.window.getHeight() - (2 * self.player.getHeight()))
                    self.misc = [self.ball, self.player, self.title, self.level,self.score,self.lives, self.nextlevel]
                    if self.chkspace(self.window.getKeys()):
                        self.ball.randomdirection()
                        self.misc.pop()
                        next_level = False
                else:
                    # Move blocks around for level 2
                    if self.level.getvalue() >= 2:
                        for block in self.onscreen:
                            block.blockmoves(self.level.getvalue(),move[(max_move//30)%2])
                        max_move += 1

                    # Bounce and checking for losing a life
                    bounce = self.ball.bouncearound(bounce)
                    if bounce == -1:
                        self.lives.remove_from_Value()
                        if self.lives.getvalue() == 0:
                            continue
                        self.ball.setmiddle()
                        halt = True
                        continue


                    for block in self.onscreen:
                        bounce = block.checkCollision(self.ball)
                        if block.checkHit():
                            self.score.add_to_Value()
                            if bounce == 1:
                                self.ball.bouncehorizontal()
                            elif bounce == 2:
                                self.ball.bouncevertical()

                    for block in self.onscreen: # Clearing the onscreen array from hit blocks since apparently its bad to remove item while iterating
                        if block.checkHit():
                            self.onscreen.remove(block)

                    if len(self.onscreen) == 0: #
                        self.level.add_to_Value()
                        self.createblocks()
                        for block in self.onscreen:
                            block.hit = False
                            self.ball.setmiddle()
                        next_level = True
                        continue

                    self.player.move(self.window.getKeys())

                    if 1 == self.player.checkCollision(self.ball): # Hits the top flat surface of paddle
                        self.ball.bouncevertical()
                    elif 2 == self.player.checkCollision(self.ball): # Hits the side of paddle... So technically doesnt bounce ball back up... Will lose a life
                        self.ball.bouncehorizontal()


            # Outputs

            self.window.clearscreen()

            if self.level.getvalue() >= 1 and self.lives.getvalue() > 0 and not halt:
                for block in self.onscreen:
                    self.window.blitSprite(block)

            for item in self.misc:
                self.window.blitSprite(item)

            self.window.updatescreen()

    def chkspace(self,keys):
        if keys[K_SPACE] == 1:
            return True

    def chk_y(self,keys):
        if keys[K_y] == 1:
            return True
