from pygame import *
import pygame_menu
import time as t

sy = 4
sx = 3

wscr = 3

s1 = 0
s2 = 0

init()
win = display.set_mode((700, 500))


def start_the_game():
    global s1, s2

    class Gs(sprite.Sprite):
        def __init__(self, player_img, player_x, player_y, player_w, player_h, player_speed):
            super().__init__()
            self.image = transform.scale(
                image.load(player_img), (player_w, player_h))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

        def reset(self):
            win.blit(self.image, (self.rect.x, self.rect.y))

    class Player(Gs):
        def rocket2(self):
            key_pressed = key.get_pressed()
            if key_pressed[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if key_pressed[K_DOWN] and self.rect.y < 630:
                self.rect.y += self.speed

        def rocket1(self):
            key_pressed = key.get_pressed()
            if key_pressed[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if key_pressed[K_s] and self.rect.y < 630:
                self.rect.y += self.speed

        def ball(self):
            global sx, sy
            self.rect.x += sx
            self.rect.y += sy
    #        print(self.rect.y)
            if self.rect.y > 450 or self.rect.y < 0:
                sy *= -1

    def scr_count():
        global s1, s2
        if sprite.collide_rect(r1, ball):
            s1 += 1
        if sprite.collide_rect(r2, ball):
            s2 += 1
    display.set_caption('Ping Pong')

    r1 = Player('racket1.png',
                10, 250, 20, 60, 4)
    r2 = Player('racket2.png',
                675, 250, 20, 60, 4)

    ball = Player('ball.png', 350, 250, 45, 45, 0)

    clock = time.Clock()
    fps = 60

    font1 = font.SysFont('ComicSansMC', 70)
    lose1 = font1.render('Player 1 Lose', True, (150, 150, 150))
    lose2 = font1.render('Player 2 Lose', True, (150, 150, 150))
    win1 = font1.render('Player 1 Wins', True, (150, 150, 150))
    win2 = font1.render('Player 2 Wins', True, (150, 150, 150))

    game = True
    fin = False

    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    game = False
        if not fin:
            # ?win.fill((155, 0, 255))
            win.fill((64, 105, 144))
            # ?win.fill((255, 255, 255))

            score1 = font1.render(str(s1), True, (0, 0, 0))
            score2 = font1.render(str(s2), True, (0, 0, 0))

            scr_count()

            ball.ball()
            r1.rocket1()
            r2.rocket2()
            r1.reset()
            r2.reset()
            ball.reset()
            win.blit(score1, (250, 50))
            win.blit(score2, (450, 50))

            if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball):
                global sx, sy
                sx *= -1

            if ball.rect.x > 675:
                fin = True
                s1 = 0
                s2 = 0
                win.blit(lose2, (200, 200))
            if ball.rect.x < 0:
                fin = True
                s1 = 0
                s2 = 0
                win.blit(lose1, (200, 200))
            if s1 >= wscr:
                fin = True
                s1 = 0
                s2 = 0
                win.blit(win1, (200, 200))
            if s2 >= wscr:
                fin = True
                s1 = 0
                s2 = 0
                win.blit(win2, (200, 200))

        display.update()
        clock.tick(fps)


m = pygame_menu.Menu('Welcome!', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

m.add.text_input('Name: ', default='Clara Oswald')
#!m.add.selector('Difficulty:', [('Hard', 1), ('easy', 2)])
m.add.button('Play', start_the_game)
m.add.button('Quit', pygame_menu.events.EXIT)

m.mainloop(win)
