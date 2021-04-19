from pygame import *

FPS = 60
clock = time.Clock()
game = True
w = 700
h = 500

window = display.set_mode((w, h))
display.set_caption("hungry cow")

background = transform.scale(image.load("back.png"), (700, 500))
window.blit(background, (0, 0))

class GameSprite((sprite.Sprite)):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Cow(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < w - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < h - 80:
            self.rect.y += self.speed

cow = Cow("cow2.png", 330, 200, 4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    cow.reset()
    cow.update()
    display.update()

        
    clock.tick(FPS)