import pygame
import sys
from settings import * 

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCEEN_HEIGHT))
        pygame.display.set_caption("Chess Game Python")
        self.board = Board()

    def run(self):
        self.handleEvents()
        self.update()
        self.draw()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw(self):
        self.screen.fill("green")
        self.board.draw(self)


    def update(self):
        pygame.display.update()
        self.clock.tick(60)

class Board:
    def __init__(self):
        self.board = [8, 8]

    def draw(self, game):
        for i in range(8):
            for j in range(8):
                farbe = (255, 255, 255) if (i + j) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(game.screen, farbe, (j * FIELD_SIZE, i * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
