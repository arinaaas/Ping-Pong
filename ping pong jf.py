from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

back = (2,250, 172)
win_widht = 700
win_height = 600
window = display.set_mode((win_widht, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)