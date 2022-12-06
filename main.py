import pygame, sys, time
from settings import *
from level import Level

class Game:
    def __init__(self):
		
		# setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Mimi <3") # Set Window Title
        self.level = Level()

    def run(self):
        while True:  
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            # game logic
            self.screen.fill('black') 
            self.level.run()               
            pygame.display.update()
            self.clock.tick(FPS)	

if __name__ == '__main__':
	game = Game()
	game.run()