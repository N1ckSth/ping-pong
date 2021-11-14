from pygame import *

sy = 3
sx = 3

class Gs(sprite.Sprite):
    def __init__ (self, player_img, player_x, player_y, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (player_w, player_h))
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

win = display.set_mode((700, 500))
display.set_caption('Ping Pong')


r1 = Player('racket.png', 10, 250, 20, 60, 3)
r2 = Player('racket.png', 675, 250, 20, 60, 3)

ball = Player('ball.png', 350, 250, 45, 45, 0)

clock = time.Clock()
fps = 60

game = True
fin = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not fin:
        #?win.fill((155, 0, 255))
        #?win.fill((141, 10, 60))
        win.fill((255, 255, 255))
        r1.rocket1()
        r2.rocket2()
        ball.ball()
        r1.reset()
        r2.reset()
        ball.reset()

    display.update()
    clock.tick(fps)