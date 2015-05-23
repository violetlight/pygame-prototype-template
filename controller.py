import pygame, sys
from constants import *

class Controller(object):
    """This is a general controller object/interface for the program."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(SCREEN["SIZE"])
        pygame.display.set_caption(SCREEN["CAPTION"])

    def loop(self):
        """This is the infinite loop of the program."""
        while True:
            self.screen.fill((200,200,12))
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(SCREEN["FPS"])
