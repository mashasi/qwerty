from pygame import *

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

class Meat(GameSprite):
    def update(self):
        

w = 700
h = 500
FPS = 60

cow =  Cow("cow2.png", 0, 0, 4)
meat = Meat("meat.png", 0, 0)
cons = Cons("cons2.png", 0, 0)

window = display.set_mode((w, h))
display.set_caption("hungry cow")
background = transform.scale(image.load("back.jpg"), (w, h))
