import pygame

class Sound:
    def __init__(self, screen):
        self.screen = screen

        self.BGM = pygame.mixer.Sound('sound/BGM.mp3')
        self.gameoverSound = pygame.mixer.Sound('sound/gameover.mp3')
        self.hitSound = pygame.mixer.Sound('sound/hit.wav')
        self.shieldSound = pygame.mixer.Sound('sound/get_shield.wav')
        self.itemSound = pygame.mixer.Sound('sound/get_item.wav')

    def playHit(self):
        self.hitSound.play()

    def playShield(self):
        self.shieldSound.play()

    def playItem(self):
        self.itemSound.play()

    def playGameover(self):
        self.gameoverSound.play()

    def stopGameover(self):
        self.gameoverSound.stop()

    def playBGM(self):
        self.BGM.play(-1)

    def stopBGM(self):
        self.BGM.stop()