import pygame
import random

class Item:
    def __init__(self, screen, pl, so):
        self.screen = screen
        
        self.last = pygame.time.get_ticks()
        self.cooldown = 10000

        self.pl = pl
        self.so = so

        self.item_img = pygame.image.load('resource/item.png')

        self.screen_width = self.screen.get_size()[0]
        self.screen_height = self.screen.get_size()[1]
        self.item_width = self.item_img.get_size()[0]
        self.item_height = self.item_img.get_size()[1]

        self.Ix_pos = random.randrange(0, self.screen_width - self.item_width)
        self.Iy_pos = random.randrange(800, 1200)

        self.speed = 5
        self.randomCount = random.randrange(800, 1500)

        self.isTouch = False
        self.isShow = True    
        self.i = 0

    def draw(self):
        if not self.isTouch and self.isShow:
            self.screen.blit(self.item_img, (self.Ix_pos, self.Iy_pos))

    def update(self):
        self.Iy_pos -= self.speed

        if self.Iy_pos <= 0 - self.item_height:
            self.Ix_pos = random.randrange(0, self.screen_width - self.item_width)
            self.Iy_pos = random.randrange(800, 1200)

        if self.Ix_pos >= self.pl.x_pos and self.Ix_pos <= self.pl.x_pos + 50:
            if self.Iy_pos >= self.pl.y_pos and self.Iy_pos <= self.pl.y_pos + 50:
                self.so.playItem()
                self.isTouch = True
                self.isShow = False
                
        if self.Ix_pos + 40 < self.pl.x_pos + 50 and self.Ix_pos + 40 > self.pl.x_pos:
            if self.Iy_pos + 40 < self.pl.y_pos + 50 and self.Iy_pos + 40 > self.pl.y_pos:
                self.so.playItem()
                self.isTouch = True
                self.isShow = False

        if self.i >= self.randomCount:
            self.Ix_pos = random.randrange(0, self.screen_width - self.item_width)
            self.Iy_pos = random.randrange(800, 1200)
            self.isShow = True
            self.i = 0
            self.randomCount = random.randrange(800, 1500)
            print("아이템 등장")