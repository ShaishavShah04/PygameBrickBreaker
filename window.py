# 2020 - 05 - 25
# Shaishav Shah

"""
Window frame for the break out game
"""

from loader import *
import pygame


class Window:
    def __init__(self):
        self.title = TITLE
        self.fps = FPS
        self.height = HEIGHT
        self.width = WIDTH
        self.screenDimensions = (self.width, self.height)
        self.background = GREY
        self.frame = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screenDimensions)
        self.screen.fill(self.background)
        self.caption = pygame.display.set_caption(self.title)
        self.keysPressed = None

    # --- Modify

    def run(self):
        while True:
            # --- Inputs
            self.getEvents()
            # -- Processing
            # -- Outputs
            self.clearscreen()
            self.updatescreen()

    def updatescreen(self):
        self.frame.tick(self.fps)
        pygame.display.flip()

    def clearscreen(self):
        self.screen.fill(self.background)

    def blitSprite(self, sprite):
        self.screen.blit(sprite.getSprite(), sprite.getPOS())

    # -- Get
    def getKeys(self):
        return self.keysPressed

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.keysPressed = pygame.key.get_pressed()

    def getWidth(self):
        return self.screen.get_rect().width

    def getHeight(self):
        return self.screen.get_rect().height


if __name__ == "__main__":
    pygame.init()

    window = Window()
    window.run()

