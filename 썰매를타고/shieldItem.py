import pygame
import random

class Shield:
    def __init__(self, screen, pl, so):
        self.screen = screen

        self.last = pygame.time.get_ticks()
        self.cooldown = 10000

        self.pl = pl
        self.so = so

        self.shield_img = pygame.image.load('resource/shieldItem.png')

        self.screen_width = self.screen.get_size()[0]
        self.screen_height = self.screen.get_size()[1]
        self.shield_width = self.shield_img.get_size()[0]
        self.shield_height = self.shield_img.get_size()[1]

        self.SIx_pos = random.randrange(0, self.screen_width - self.shield_width)
        self.SIy_pos = random.randrange(800, 2000)

        self.speed = 5

        self.isTouch = False
        self.isShow = True    
        self.i = 0

    def draw(self):
        if not self.isTouch and self.isShow:
            self.screen.blit(self.shield_img, (self.SIx_pos, self.SIy_pos))

    def update(self):
        self.SIy_pos -= self.speed

        if self.SIy_pos <= 0 - self.shield_height:
            self.SIx_pos = random.randrange(0, self.screen_width - self.shield_width)
            self.SIy_pos = random.randrange(800, 2000)

        if self.SIx_pos >= self.pl.x_pos and self.SIx_pos <= self.pl.x_pos + 50:
            if self.SIy_pos >= self.pl.y_pos and self.SIy_pos <= self.pl.y_pos +50:
                self.so.playShield()
                self.isTouch = True
                self.isShow = False

        if self.SIx_pos + 40 < self.pl.x_pos + 50 and self.SIx_pos + 40 > self.pl.x_pos:
            if self.SIy_pos + 40 < self.pl.y_pos + 50 and self.SIy_pos + 40 > self.pl.y_pos:
                self.so.playShield()
                self.isTouch = True
                self.isShow = False

       
        if self.i >= 1500:
            self.now = pygame.time.get_ticks()
            if self.now - self.last >= self.cooldown:
                self.SIy_pos = random.randrange(800, 1200)
                self.SIx_pos = random.randrange(0, self.screen_width - self.shield_width)
                self.last = self.now
                self.isShow = True
                self.isTouch = False
                print("방패 아이템 등장")
                self.i = 0