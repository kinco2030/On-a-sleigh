import pygame

class Background:
    def __init__(self, screen):
        self.screen = screen
        self.bg_img1 = pygame.image.load("resource/background.png")
        self.bg_img2 = pygame.image.load("resource/background.png")

        self.start_ticks = pygame.time.get_ticks()

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 800

        self.speed = 5

    def draw(self):
        self.screen.blit(self.bg_img1, (self.x1, self.y1))
        self.screen.blit(self.bg_img2, (self.x2, self.y2))

    def update(self):
        self.y1 += -self.speed 
        self.y2 += -self.speed 

        if self.y1 <= -800:
            self.y1 = 800
        if self.y2 <= -800:
            self.y2 = 800