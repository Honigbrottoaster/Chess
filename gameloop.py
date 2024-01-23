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
        self.board.draw(self)


    def update(self):
        self.board.loadPositionFromFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        pygame.display.update()
        self.clock.tick(60)

class Board:
    def __init__(self):
        self.board = [8, 8]

    def loadPositionFromFEN(self, fen):
        split_fen = fen.split()
        for row in split_fen[0].split('/'):
            for char in row:
                if char == 'p':
                    print("Schwarzer Bauer gefunden")

    def draw(self, game):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = (255, 255, 255) 
                else: 
                    color = (169, 169, 169)
                pygame.draw.rect(game.screen, color, (j * FIELD_SIZE, i * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
