import sys
import pygame

#CREATING A PYGAME WINDOW

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__=='__main__':
    ai =AlienInvasion()
    ai.run_game()

#FRAME RATE

    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()


    def run_game(self):
        while True:
            pygame.display.flip()
            self.clock.tick(60)


#BACKGROUND COLOR

    def __init__(self):
        pygame.display.set_caption("Alien Invasion")
        self.bg_color=(230,230,230)

    def run_game(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()


        self.screen.fill(self.bg_color)
        pygame.display.flip()
        self.clock.tick(60)



