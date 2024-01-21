import pygame
import random

class Snowman:
    def __init__(self, screen):
        self.screen = screen

        self.snowman = pygame.image.load("resource/snowman.png")

        self.screen_width = self.screen.get_size()[0]
        self.screen_height = self.screen.get_size()[1]
        self.snowman_width = self.snowman.get_size()[0]
        self.snowman_height = self.snowman.get_size()[1]

        self.Sx_pos = random.randrange(0, self.screen_width - self.snowman_width)
        self.Sy_pos = random.randrange(800, 1500)

        self.start_ticks = pygame.time.get_ticks()
        self.speed = 5


    def draw(self):
        self.screen.blit(self.snowman, (self.Sx_pos, self.Sy_pos))

    def update(self):
        self.Sy_pos -= self.speed

        if self.Sy_pos <= 0 - self.snowman_height:
            self.Sx_pos = random.randrange(0, self.screen_width - self.snowman_width)
            self.Sy_pos = random.randrange(800, 1500)