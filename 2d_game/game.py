import pygame

from pygame.locals import QUIT


class Game:
    running = False

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([500, 500])

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))

            pygame.display.flip()

        if self.running is False:
            pygame.quit()


game = Game()
game.run()
