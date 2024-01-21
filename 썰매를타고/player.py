import pygame

class Player:
    def __init__(self, screen, tr, sn, so):
        self.screen = screen
        self.tr = tr
        self.sn = sn
        self.so = so
        
        self.gameover = False

        self.player = [pygame.image.load("resource/player1.png"),
                       pygame.image.load("resource/player2.png"),
                       pygame.image.load("resource/player3.png"),
                       pygame.image.load("resource/player_s_1.png"),
                       pygame.image.load("resource/player_s_2.png")]

        self.screen_width = self.screen.get_size()[0]
        self.screen_height = self.screen.get_size()[1]

        self.x_pos = (self.screen_width / 2) - (50 / 2)
        self.y_pos = -50

        self.is_turn = 3
        self.shield = False

    def draw(self):
        if self.is_turn == 3:
            self.screen.blit(self.player[0], (self.x_pos, self.y_pos))
        if self.is_turn == 0:
            self.screen.blit(self.player[1], (self.x_pos, self.y_pos))
        if self.is_turn == 1:
            self.screen.blit(self.player[2], (self.x_pos, self.y_pos))
        if self.shield:
            if self.is_turn == 0:
                self.screen.blit(self.player[4], (self.x_pos, self.y_pos))
            elif self.is_turn == 1:
                self.screen.blit(self.player[3], (self.x_pos, self.y_pos))

    def update(self):
        if self.is_turn == 3:
            self.x_pos = (self.screen_width / 2) - (50 / 2)
            self.y_pos += 4
            if self.y_pos >= 120:
                self.y_pos = 120
        elif self.is_turn == 0:
            self.x_pos -= 4
            self.y_pos += 4
            if self.y_pos >= 120:
                self.y_pos = 120
        elif self.is_turn == 1:
            self.x_pos += 4
            self.y_pos += 4
            if self.y_pos >= 120:
                self.y_pos = 120

        if self.x_pos <= 0:
            self.x_pos = 0
            print("벽과 충돌함")
            self.so.playHit()
            pygame.time.delay(1000)
            self.gameover = True
        elif self.x_pos >= self.screen_width - 50:
            self.x_pos = self.screen_width - 50
            print("벽과 충돌함")
            self.so.playHit()
            pygame.time.delay(1000)
            self.gameover = True

        if self.shield:
            # 나무 충돌
            for self.s in self.tr:
                if self.x_pos > self.s.Tx_pos and self.x_pos <= self.s.Tx_pos + 40:
                    if self.y_pos > self.s.Ty_pos and self.y_pos <= self.s.Ty_pos + 40:
                        print("충돌 무시")

                if self.x_pos + 50 < self.s.Tx_pos + 40 and self.x_pos + 50 > self.s.Tx_pos:
                    if self.y_pos + 50 < self.s.Ty_pos + 40 and self.y_pos + 50 > self.s.Ty_pos:
                        print("충돌 무시")

            # 눈사람 충돌
            for self.s in self.sn:
                if self.x_pos > self.s.Sx_pos and self.x_pos <= self.s.Sx_pos + 40:
                    if self.y_pos > self.s.Sy_pos and self.y_pos <= self.s.Sy_pos + 40:
                        print("충돌 무시")

                if self.x_pos + 50 < self.s.Sx_pos + 40 and self.x_pos + 50 > self.s.Sx_pos:
                    if self.y_pos + 50 < self.s.Sy_pos + 40 and self.y_pos + 50 > self.s.Sy_pos:
                        print("충돌 무시")
        else:
            # 나무 충돌
            for self.s in self.tr:
                if self.x_pos > self.s.Tx_pos and self.x_pos <= self.s.Tx_pos + 30:
                    if self.y_pos > self.s.Ty_pos and self.y_pos <= self.s.Ty_pos + 30:
                        print("충돌함")
                        self.so.playHit()
                        pygame.time.delay(1000)
                        self.gameover = True

                if self.x_pos + 30 < self.s.Tx_pos + 30 and self.x_pos + 30 > self.s.Tx_pos:
                    if self.y_pos + 30 < self.s.Ty_pos + 30 and self.y_pos + 30 > self.s.Ty_pos:
                        print("충돌함")
                        self.so.playHit()
                        pygame.time.delay(1000)
                        self.gameover = True

            # 눈사람 충돌
            for self.s in self.sn:
                if self.x_pos > self.s.Sx_pos and self.x_pos <= self.s.Sx_pos + 20:
                    if self.y_pos > self.s.Sy_pos and self.y_pos <= self.s.Sy_pos + 20:
                        print("충돌함")
                        self.so.playHit()
                        pygame.time.delay(1000)
                        self.gameover = True

                if self.x_pos + 30 < self.s.Sx_pos + 20 and self.x_pos + 30 > self.s.Sx_pos:
                    if self.y_pos + 30 < self.s.Sy_pos + 20 and self.y_pos + 30 > self.s.Sy_pos:
                        print("충돌함")
                        self.so.playHit()
                        pygame.time.delay(1000)
                        self.gameover = True