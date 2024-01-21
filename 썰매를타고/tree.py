import pygame
import random

class Tree:
    def __init__(self, screen):
        self.screen = screen

        self.tree = pygame.image.load("resource/tree.png")

        self.screen_width = self.screen.get_size()[0]
        self.screen_height = self.screen.get_size()[1]
        self.tree_width = self.tree.get_size()[0]
        self.tree_height = self.tree.get_size()[1]

        self.Tx_pos = random.randrange(0, self.screen_width - self.tree_width)
        self.Ty_pos = random.randrange(800, 1500)

        self.start_ticks = pygame.time.get_ticks()
        self.speed = 5

    def draw(self):
        self.screen.blit(self.tree, (self.Tx_pos, self.Ty_pos))

    def update(self):
        self.Ty_pos -= self.speed

        if self.Ty_pos <= 0 - self.tree_height:
            self.Tx_pos = random.randrange(0, self.screen_width - self.tree_width)
            self.Ty_pos = random.randrange(800, 2000)