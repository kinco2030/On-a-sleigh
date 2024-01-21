import pygame
import background, player, tree, item, snowman, shieldItem, sound

pygame.init()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("게ㅔㅔㅔㅔㅔㅔㅔ임")
tr = []
sn = []
clock = pygame.time.Clock()

def intro():
    intro_img = pygame.image.load("resource/intro_img.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    return 1
        
        screen.blit(intro_img, (0, 0))
        pygame.display.update()

def gameDescription():
    description_img = pygame.image.load("resource/description.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    return 1

        screen.blit(description_img, (0, 0))
        pygame.display.update()
            

def gameover(score):
    so = sound.Sound(screen)
    gameover_img = pygame.image.load('resource/gameover.png')
    so.playGameover()
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont(None, 50)
    score_text = font.render("score:"+str(score//10), True, BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_r:
                    so.stopGameover()
                    main()
        screen.blit(gameover_img, (0, 0))
        screen.blit(score_text, (190, 355))
        pygame.display.update()


def main():
    font = pygame.font.SysFont(None, 45)
    score = 0
    count = 3

    # 나중에 숫자 바꾸기
    tree_list = [1,2,3,4]
    snow_list = [1,2,3]
    
    so = sound.Sound(screen)
    bg = background.Background(screen)

    for x in tree_list :
        tr.append(tree.Tree(screen))

    for x in snow_list:
        sn.append(snowman.Snowman(screen))

    pl = player.Player(screen, tr, sn, so)
    it = item.Item(screen, pl, so)
    si = shieldItem.Shield(screen, pl, so)

    it.isTouch = False
    si.isTouch = False
    pl.shield = False

    so.playBGM()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    if count == 3:
                        pl.is_turn = 1
                        count = 0 
                    elif count == 0:
                        pl.is_turn = 0
                        count = 1
                    elif count == 1:
                        pl.is_turn = 1
                        count = 0

        score += 1

        if it.isTouch:
            nowScore = score
            nowScore += 50
            score = nowScore
            it.isTouch = False

        if not it.isShow:
            it.i += 1

        if si.isTouch:
            pl.shield = True 
            si.i += 1
            
        if si.i >= 500:
            pl.shield = False 

        text = font.render("score:"+str(score//10), True, (0, 0, 0))

        if 500 <= score // 10 < 1000 :
            bg.speed = 7
            it.speed = 7
            si.speed = 7
            for t in tr:
                t.speed = 7
            for s in sn:
                s.speed = 7
        elif 1000 <= score // 10 < 1500:
            bg.speed = 9
            it.speed = 9
            si.speed = 9
            for t in tr:
                t.speed = 9
            for s in sn:
                s.speed = 9
        elif 1500 <= score // 10 < 2000:
            bg.speed = 11
            it.speed = 11
            si.speed = 11
            for t in tr:
                t.speed = 11
            for s in sn:
                s.speed = 11
        elif 2000 <= score // 10 < 2500:
            bg.speed = 13
            it.speed = 13
            si.speed = 13
            for t in tr:
                t.speed = 13
            for s in sn:
                s.speed = 13
        elif 2500 <= score // 10:
            bg.speed = 15
            it.speed = 15
            si.speed = 15
            for t in tr:
                t.speed = 15
            for s in sn:
                s.speed = 15

        if pl.gameover:
            so.stopBGM()
            tr.clear()
            sn.clear()
            gameover(score)

        bg.draw()
        bg.update()
        pl.draw()
        pl.update()
        it.draw()
        it.update()
        si.draw()
        si.update()
        for x in sn:
            x.draw()
            x.update()
        for x in tr:
            x.draw()
            x.update()

        clock.tick(60)
        screen.blit(text, (10, 10))
        pygame.display.update()

intro()
gameDescription()
main()